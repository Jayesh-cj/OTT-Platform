from datetime import date, datetime
import re
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import redirect, render

from Admin.models import *
from Guest.models import *
from User.models import *
from django.db.models import Q
# Create your views here.


def check_subscription(uid):
    subscribed = tbl_subscription.objects.filter(subscription_status=1, user_id=uid).count()
    if subscribed > 0:
        return True
    else:
        return False
    

def check_age(uid):
    user_dob = tbl_user.objects.get(id=uid).user_dob
    # Calculate today's date
    today = date.today()
    # Calculate the age
    age = today.year - user_dob.year - ((today.month, today.day) < (user_dob.month, user_dob.day))
    # if age < 18:
    #     return False
    # else:
    #     return True
    return age


# Homepage
def homepage(request):
    first = tbl_content_details.objects.first()
    content_details = tbl_content_details.objects.all()
    new_arrivals = tbl_content_details.objects.order_by('-id')
    user=request.session["uid"]
    subscribed = check_subscription(user)
    mager = check_age(user)

    return render(request,'User/Homepage.html',{
        'Details':content_details,
        'Subscribed':subscribed,
        'New':new_arrivals,
        'First':first,
        'Mager':mager
    })


# My Profile 
def show_profie(request):
    user = tbl_user.objects.get(id=request.session["uid"])
    return render(request,'User/MyProfile.html',{
        'User':user
    })


# Edit Profile 
def edit_profile(request):
    User = tbl_user.objects.get(id=request.session["uid"])
    if request.method == 'POST':
        User.user_name = request.POST.get('txt_name')
        User.user_contact = request.POST.get('txt_contact')
        User.user_email = request.POST.get('txt_email')
        User.save()
        return redirect('webuser:show_profile')
    else:
        return render(request,'User/EditProfile.html',{
            'Details':User
        })


# Change Password 
def change_password(request):
    if request.method == 'POST':
        user = tbl_user.objects.get(id=request.session["uid"])
        
        current = request.POST.get("txt_current_password")
        new = request.POST.get("txt_new_password")
        confirm = request.POST.get("txt_confirm_password")

        if current == user.user_password:
            if new == confirm:
                user.user_password = new
                user.save()
            else:
                msg = "Password Incorrect!"
                return render(request,'User/ChangePassword.html',{
                    'msg':msg
                })
        else:
            msg = "Password Missmatch!"
            return render(request,'User/ChangePassword.html',{
                'msg':msg
            })
        
    return render(request,'User/ChangePassword.html')


# View Package Deatails
def view_package_deatails(request):
    pacakge_details=tbl_package.objects.all()
    if request.method == 'POST':
        pid = request.POST.get('package_id')
        # print("pakage")
        # print(pid)
        return render(request,'User/Payment.html',{
            'pid':pid
        })
    else:
        return render(request,'User/ViewPackages.html',{
            'Package':pacakge_details
        })


# Payment
def payment(request):
    return render(request,'User/Payment.html')


# Subscribe Package
def subscribe_package(request,pid):
    pacakge_details=tbl_package.objects.all()
    user = tbl_user.objects.get(id=request.session["uid"])
    pack = tbl_package.objects.get(id=pid)
    subscription, status = tbl_subscription.objects.get_or_create(
        user_id=user,
        package_id=pack,
        subscription_date=date.today(),
        # subscription_status=1
    )
    # print(subscription)
    # print(status)
    if status:
        subscription.subscription_status=1
        subscription.save()
    else:
        subscription.subscription_status=1
        subscription.save()

    return redirect('webuser:homepage')
    # return render(request,'User/ViewPackages.html',{
    #     'Package':pacakge_details
    # })


# Add Genres 
def add_genre(request):
    if request.method == 'POST':
        tbl_genre.objects.create(
            genre_name = request.POST.get('txt_genre')
        )
        return redirect('webuser:add_users_contents_details')
    else:
        return render(request,'User/AddGenre.html')


# Upload User Contets 
def add_content_details(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    category_data=tbl_category.objects.order_by("category_name")
    language_data=tbl_language.objects.order_by("language_name")
    genre=tbl_genre.objects.order_by("genre_name")

    if request.method == 'POST':

        cat_id=tbl_category.objects.get(id=request.POST.get("sel_category"))
        lang_id=tbl_language.objects.get(id=request.POST.get("sel_language"))
        selectedgenre=request.POST.getlist("check_genre[]")
        genres = tbl_genre.objects.filter(id__in=selectedgenre)
        genre_names = [genre.genre_name for genre in genres]


        tbl_content_details.objects.create(
            details_photo=request.FILES.get("file_poster"),
            details_title=request.POST.get("txt_content_title"),
            details_description=request.POST.get("txt_content_description"),
            details_certificate=request.POST.get("sel_certificate"),
            category_id=cat_id,
            language_id=lang_id,
            details_genres=','.join(genre_names),
            details_filesize = request.POST.get("sel_file_type"),
            user_id = user
        )
        return redirect('webadmin:homepage')

    return render(request,'User/AddContentDetails.html',{
        'Category':category_data,
        'Language':language_data,
        'Genre':genre
    })


# Upload Users Contents 
def add_content(request):
    content_title = tbl_content_details.objects.order_by('-id')
    if request.method == 'POST':
        details=tbl_content_details.objects.get(id=request.POST.get("sel_title"))
        tbl_content.objects.create(
            content_file=request.FILES.get("file_content_movie"),
            content_duration=request.POST.get("time_duration"),
            content_release_date=request.POST.get("date_release"),
            details_id=details
        )
        return redirect('webuser:homepage')
    else:
        return render(request,'User/AddContent.html',{
            'Title':content_title
        })
    

# Upload Series 
def add_series(request):
    content_details = tbl_content_details.objects.order_by("-id")

    if request.method == 'POST':
        details = tbl_content_details.objects.get(id=request.POST.get("sel_title"))
        tbl_content.objects.create(
            content_season = request.POST.get("num_season"),
            content_episode  = request.POST.get("num_episode"),
            content_file = request.FILES.get("file_series"),
            content_title = request.POST.get("txt_episode_title"),
            content_description = request.POST.get("txt_episode_description"),
            content_release_date = request.POST.get("date_release_date"),
            content_duration = request.POST.get("txt_duration"),
            details_id = details
        )
        msg="Episode Added"
        return render(request,'User/AddSeries.html',{
            'Details':content_details,
            'msg':msg
        })
    return render(request,'User/AddSeries.html',{
        'Details':content_details
    })
    


# Upload Crew Details 
def add_crew_details(request):
    return render(request,'User/AddCrewDetails.html')


# Upload Trailer 
def add_trailer(request):
    content_data = tbl_content_details.objects.order_by("-id")
    if request.method == 'POST':

        content = tbl_content_details.objects.get(id=request.POST.get("sel_content"))
        # print(request.POST.get("txt_url"))
        content.trailer_id = request.POST.get("sel_content")
        tbl_trailer.objects.create(
            trailer_release_date=request.POST.get("date_release_date"),
            # trailer_duration=request.POST.get("time_duration"),
            trailer_url=request.POST.get("txt_url"),
            details_id=content
        )
        return redirect('webuser:homepage')
        
    return render(request,'User/AddContentTrailer.html',{
        'Content':content_data
    })
    

# Check Uploaded Contents Status 
def check_content_ststus(request):
    user = request.session['uid']
    # print(user)
    details = tbl_content_details.objects.filter(user_id = user)
    return render(request,'User/UserContentStatus.html',{
        'Details':details
    })


# All Contents Display 
def all_contents_display(request):
    details = tbl_content_details.objects.all()
    return render(request,'User/AllContents.html',{
        'Details':details
    })

# Display Content Details 
def content_details(request,cid):
    user = request.session['uid']
    user_age = check_age(user)

    # user = tbl_user.objects.get(request.session['uid'])
    content_details = tbl_content_details.objects.get(id=cid)
    watchlist = tbl_watchlist.objects.filter(user_id=request.session['uid'])

    if content_details.details_filesize == 0:
        single = True

        crew_details = tbl_crew.objects.filter(details_id=cid)
        content = tbl_content.objects.get(details_id=cid)

        return render(request,'User/ContentDetails.html',{  
            'Single':single,          
            'Details':content_details,
            'Content':content,
            'Crew':crew_details,
            'Watchlist':watchlist,
            'user_age':user_age
        })
    else:
        single = False

        # content_details = tbl_content_details.objects.get(id=cid)
        series_list = tbl_content.objects.filter(details_id=cid)
        print(series_list[0].id)
        play = series_list[0].id
        return render(request,'User/SeriesList.html',{
            'List':series_list,
            'Details':content_details,
            'Watchlist':watchlist,
            'pid':play
        })



# Create Watch List 
def create_watchlist(request):
    playlist = tbl_watchlist.objects.all()
    user = tbl_user.objects.get(id=request.session['uid'])

    if request.method == 'POST':
        tbl_watchlist.objects.create(
            watchlist_name = request.POST.get("txt_title"),
            user_id = user
        )
        msg = "Playlist Created"
        return render(request,'User/Watchlist.html',{
            'msg':msg
        })
    else:
        return render(request,'User/Watchlist.html',{
            'Watchlist':playlist
        })


# Add Content into Watchlist 
def add_content_in_watchlit(request,wid,cid):
    # print(date.today())
    watchlist = tbl_watchlist.objects.get(id=wid)
    content = tbl_content_details.objects.get(id=cid)
    
    tbL_watchlist_content.objects.create(
        wlist_date = date.today(),
        watchlist_id = watchlist,
        details_id = content
    )
    return render(request,'User/Watchlist.html')

# View Watchlist Contents 
def view_watchlist_contents(request,wid):
    user = tbl_user.objects.get(id=request.session['uid'])
    list_contents = tbL_watchlist_content.objects.filter(watchlist_id = wid)
    return render(request,'User/WatchlistContents.html',{
        'ContentList':list_contents
    })


# Crew Details Insert 
def crew_details(request,cid):
    crew_details = tbl_crew.objects.get(id=cid)
    return render(request,'User/CrewDetails.html',{
        'Crew':crew_details
    })

# Episode Details 
def episode_details(request,cid):
    episode_details = tbl_content.objects.get(id=cid)
    return render(request,'User/EpisodeDetails.html',{
        'Details':episode_details
    })

# View Series Episode List 
# def series_episode_list(request,cid):
    

# Play Content
def play_content(request,pid):
    content = tbl_content.objects.get(id=pid)
    return render(request,'User/PlayContent.html',{
        'Content':content
    })


# View Trailers In Admin
def view_trailer(request,tid):
    data = tbl_trailer.objects.get(details_id=tid)
    link = data.trailer_url
    video_id = extract_video_id(link)
    # print("Video ID:", video_id)
    
    return render(request,'User/ViewTrailers.html',{'Trailer':video_id})

# Ecstract Video ID from You tub Video
def extract_video_id(url):
    # Regular expression to match the video ID in YouTube URLs
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([\w-]+)(?:&.*)?'

    match = re.match(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

# Example usage:
# youtube_url = "https://www.youtube.com/watch?v=U8SX5d68zUU"
# video_id = extract_video_id(youtube_url)
# print("Video ID:", video_id)


# Review Content
def review_contents(request):
    return render(request,'User/ReviewContent.html')


# View Complaints 
def view_complaints(request):
    user = request.session['uid']
    complaints = tbl_complaint.objects.filter(user_id=user)
    return render(request,'User/Complaints.html',{
        'Complaints':complaints
    })

# Complaint To Website Admin
def complaint_to_admin(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    
    if request.method == 'POST':
        tbl_complaint.objects.create(
            complaint_title = request.POST.get("txt_complaint_title"),
            complaint_content = request.POST.get("txt_complaint_content"),
            complaint_date = date.today(),
            user_id = user
        )
        return redirect('webuser:homepage')
    else:
        return render(request,'User/ComplaintToAdmin.html')


# FeedBack 
def feedback(request):
    user = tbl_user.objects.get(id=request.session['uid'])
    if request.method == 'POST':
        tbl_feedback.objects.create(
            feedback_content = request.POST.get("txt_feedback_content"),
            feedback_date = date.today(),
            user_id = user
        )
        return render(request,'User/Homepage.html')
    else:
        return render(request,'User/Feedback.html')


# Ratting 
def rating(request,cid):
    if 'uid' in request.session:
        parray=[1,2,3,4,5]
        cid=cid
        wadata=tbL_watchlist_content.objects.get(id=cid)
        cdata=tbl_content_details.objects.get(id=wadata.details_id.id)
        wdata=tbl_user.objects.get(id=request.session["uid"])
        counts=0
        counts=stardata=tbl_review.objects.filter(details_id=cdata).count()
        if counts>0:
            res=0
            stardata=tbl_review.objects.filter(details_id=cdata).order_by('-review_datetime')
            for i in stardata:
                res = res + int(i.user_rating)
                avg=res//counts  
            return render(request,"User/Rating.html",{"cid":cid,"data":stardata,"ar":parray,"avg":avg,"count":counts})
        else:
            return render(request,"User/Rating.html",{'cid':cid})
    else:
        return redirect("webguest:user_login")

def ajaxrating(request):
    parray=[1,2,3,4,5]
    user_rating=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    car=request.GET.get('workid')
    wadata=tbL_watchlist_content.objects.get(id=car)
    cdata=tbl_content_details.objects.get(id=wadata.details_id.id)
    cust=tbl_user.objects.get(id=request.session["uid"])
    tbl_review.objects.create(user_name=user_name,user_review=user_review,user_rating=user_rating,details_id=cdata,user_id=cust)
    stardata=tbl_review.objects.filter(details_id=cdata).order_by('-review_datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    car_id = request.GET.get("pdt")
    wadata=tbL_watchlist_content.objects.get(id=car_id)
    cdata = tbl_content_details.objects.get(id=wadata.details_id.id)
    rate = tbl_review.objects.filter(details_id=cdata)

    for i in rate:
        if int(i.user_rating) == 5:
            five += 1
        elif int(i.user_rating) == 4:
            four += 1
        elif int(i.user_rating) == 3:
            three += 1
        elif int(i.user_rating) == 2:
            two += 1
        elif int(i.user_rating) == 1:
            one += 1

        r_len += 1
    #print(r_len)

    rlen = r_len / 5
    #print(rlen)
    result = {"five": five, "four": four, "three": three, "two": two, "one": one, "total_review": rlen}
    return JsonResponse(result)


# Chatroom List 
def chatroom_list(request):
    list = tbl_chatroom.objects.all()
    return render(request,'User/ChatroomList.html',{
        'List':list
    })


# Create Chatrrom 
def create_chatroom(request):
    user = request.session['uid']
    # print(user)
    if request.method == 'POST':
        tbl_chatroom.objects.create(
            community_name = request.POST.get('txt_name'),
            community_photo = request.FILES.get('file_photo'),
            community_description = request.POST.get('txt_description'),
            community_date = date.today(),
            community_status = request.POST.get('status'),
            user_id = user
        )
        return redirect('webuser:chatrooms')
    else:
        return render(request,'User/CreateChatroom.html')


# Chat Room
def chatpage(request,rid):
    user  = tbl_user.objects.get(id=request.session["uid"])
    room = tbl_chatroom.objects.get(id=rid)
    # print(room.community_name)
    return render(request,"User/Chat.html",{
        "user":user,
        'Room':room
    })

def ajaxchat(request,rid):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    # to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    room = tbl_chatroom.objects.get(id=rid)
    tbl_chat.objects.create(
        chat_content=request.POST.get("msg"),
        chat_time=datetime.now(),
        user_from=from_user,
        chat_file=request.FILES.get("file"),
        room_id = room
    )
    return render(request,"User/Chat.html")


def ajaxchatview(request,rid):
    tid = request.session["uid"]
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter(room_id = rid).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})
    return render(request,"User/ChatView.html")

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"ChatApp/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})