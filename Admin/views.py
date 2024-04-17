import re
from django.shortcuts import render,redirect

from Admin.models import *
from User.models import tbl_complaint, tbl_feedback
# from User.models import tbl_user

# Create your views here.


# Homepage
def homepage(request):
    admin=tbl_admin.objects.get(id=request.session['aid'])
    c_count = tbl_content_details.objects.all().count()
    u_count = tbl_user.objects.all().count()
    cmp_count = tbl_complaint.objects.count()
    f_count = tbl_feedback.objects.all().count()
    return render(request,"Admin/Homepage.html",{
        'data':admin,
        'Content':c_count,
        'User':u_count,
        'Complaint':cmp_count,
        'Feedback':f_count,
        'Admin':admin
    })

# Change Password
def change_password(request):
    if request.method == 'POST':
        admin=tbl_admin.objects.get(id=request.session['aid'])
        current = request.POST.get("txt_current_password")
        new = request.POST.get("txt_new_password")
        confirm = request.POST.get("txt_confirm_password")
        # print(current)
        # print(new)
        # print(confirm)

        if current == admin.admin_password:
            if new == confirm:
                admin.admin_password = request.POST.get("txt_new_password")
                admin.save()
            else:
                msg = "Confirm Password!"
                return render(request,'Admin/ChangePassword.html',{
                    'msg':msg
                })
        else:
            msg = "Password Missmatch!"
            return render(request,'Admin/ChangePassword.html',{
                'msg':msg
            })
    return render(request,'Admin/ChangePassword.html',{
    })

    
# # District Insert
# def district(request):
#     dis_data=tbl_district.objects.all()
#     if request.method=='POST':
#         tbl_district.objects.create(district_name=request.POST.get("txt_district"))
#         return render(request,"Admin/District.html",{
#             'Data':dis_data,
#         })
#     else:
#         return render(request,"Admin/District.html",{
#             'Data':dis_data,
#         })

# # District Delete
# def del_district(request,did):
#     tbl_district.objects.get(id=did).delete()
#     return redirect('webadmin:district')

# # District Edit
# def edit_district(request,eid):
#     ddata=tbl_district.objects.get(id=eid)
#     dis_data=tbl_district.objects.all()
#     if request.method=="POST":
#         ddata.district_name=request.POST.get("txt_district")
#         ddata.save()
#         return redirect('webadmin:district')
#     else:
#         return render(request,"Admin/District.html",{
#             'Ddata':ddata,
#             'Data':dis_data
#         })

    
# # Place Insert
# def place(request):
#     district_data=tbl_district.objects.all()
#     place_data=tbl_place.objects.all()
#     if request.method == 'POST':
#         dis_id=tbl_district.objects.get(id=request.POST.get("sel_district"))
#         tbl_place.objects.create(
#             place_name=request.POST.get("txt_place"),
#             district_id=dis_id,
#         )
#         return render(request,'Admin/Place.html',{
#             'Ddata':district_data,
#             'PData':place_data
#         })
#     else:
#         return render(request,'Admin/Place.html',{
#             'Ddata':district_data,
#             'PData':place_data
#         })

# # Place Delete
# def del_place(request,did):
#     tbl_place.objects.get(id=did).delete()
#     return redirect("webadmin:place")

# # Place Edit
# def edit_place(request,eid):
#     dis_data=tbl_district.objects.all()
#     p_data=tbl_place.objects.all()
#     place_data=tbl_place.objects.get(id=eid)
#     if request.method == 'POST':
#         dis_id=tbl_district.objects.get(id=request.POST.get("sel_district"))
#         place_data.district_id=dis_id
#         place_data.place_name=request.POST.get("txt_place")
#         place_data.place_pin=request.POST.get("txt_pin")
#         place_data.save()
#         return redirect("webadmin:place")
#     else:
#         return render(request,'Admin/Place.html',{
#         'Place':place_data,
#         'Dis_data':dis_data,
#         'PData':p_data
#     })


# Category Insert
def category(request):
    cat_data=tbl_category.objects.order_by("category_name")
    if request.method == 'POST':
        tbl_category.objects.create(category_name=request.POST.get("txt_category"))
        return render(request,"Admin/Category.html",{
            'Cat_data':cat_data,
        })
    else:
        return render(request,"Admin/Category.html",{
            'Cat_data':cat_data,
        })

#Category Delete
def del_category(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect('webadmin:category')

# Category Edit
def edit_category(request,eid):
    cdata=tbl_category.objects.get(id=eid)
    Cat_data=tbl_category.objects.all()
    if request.method == 'POST':
        cdata.category_name=request.POST.get("txt_category")
        cdata.save()
        return redirect('webadmin:category')
    else:
        return render(request,'Admin/Category.html',{
            'Cdata':cdata,
            'Cat_data':Cat_data
    })


# Language Insert
def language(request):
    LData=tbl_language.objects.order_by("language_name")
    if request.method=='POST':
        tbl_language.objects.create(
            language_name=request.POST.get("txt_language")
        )
        return render(request,'Admin/Language.html',{
            'Data':LData
        })
    else:
        return render(request,'Admin/Language.html',{
            'Data':LData
        })

# Language Edit
def edit_language(request,eid):
    L_Data=tbl_language.objects.get(id=eid)
    LData=tbl_language.objects.all()
    if request.method=="POST":
        L_Data.language_name=request.POST.get("txt_language")
        L_Data.save()
        return redirect('webadmin:language')
    else:
        return render(request,'Admin/Language.html',{
        'Data':LData,
        'l_data':L_Data,
    })

# Language Delete
def del_language(request,did):
    tbl_language.objects.get(id=did).delete()
    return redirect('webadmin:language')


# Genre Insert
def genre(request):
    genre_data=tbl_genre.objects.order_by("genre_name")
    if request.method=="POST":
        tbl_genre.objects.create(
            genre_name=request.POST.get("txt_genre")
        )
        return redirect('webadmin:genre')
    else:
        return render(request,'Admin/Genre.html',{
            'Genre':genre_data
        })

# Genre Edit
def edit_genre(request,eid):
    edit_data=tbl_genre.objects.get(id=eid)
    genre_data=tbl_genre.objects.all()
    if request.method=="POST":
        edit_data.genre_name=request.POST.get("txt_genre")
        edit_data.save()
        return redirect('webadmin:genre')
    else:
        return render(request,'Admin/Genre.html',{
            'Genre':genre_data,
            'E_Genre':edit_data
        })

# Genre Delete
def del_genre(request,did):
    tbl_genre.objects.get(id=did).delete()
    return redirect('webadmin:genre')


# Package Create
def package(request):
    Package=tbl_package.objects.all()
    if request.method=="POST":
        tbl_package.objects.create(
            package_title=request.POST.get("txt_name"),
            package_discription=request.POST.get("txt_discription"),
            package_validity=request.POST.get("num_validity"),
            package_price=request.POST.get("num_price")
        )
        return render(request,'Admin/Package.html',{
            'Package':Package
        })
    else:
        return render(request,'Admin/Package.html',{
            'Package':Package
        })
    
# Package Edit
def edit_package(request,eid):
    Package=tbl_package.objects.all()
    edit_package=tbl_package.objects.get(id=eid)
    if request.method=="POST":
        edit_package.package_title=request.POST.get("txt_name")
        edit_package.package_discription=request.POST.get("txt_discription")
        edit_package.package_validity=request.POST.get("num_validity")
        edit_package.package_price=request.POST.get("num_price")
        edit_package.save()
        return redirect('webadmin:package')
    else:
        return render(request,'Admin/Package.html',{
            'Package':Package,
            'Edit':edit_package
        })
    
# Package Delete
def del_package(request,did):
    tbl_package.objects.get(id=did).delete()
    return redirect('webadmin:package')


# Upload

# Add Content Details
def add_content_details(request):
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
            details_status = 1,
            details_genres=','.join(genre_names),
            details_filesize = request.POST.get("sel_file_type")
        )
        return redirect('webadmin:upload_trailer') 
    
    return render(request,"Admin/AddContentDetails.html",{
        'Category':category_data,
        'Language':language_data,
        'Genre':genre
    })


# Add Content
def add_content(request):
    content_title=tbl_content_details.objects.order_by("-id")

    if request.method == 'POST':
        details=tbl_content_details.objects.get(id=request.POST.get("sel_title"))
        tbl_content.objects.create(
            content_file=request.FILES.get("file_content_movie"),
            content_duration=request.POST.get("time_duration"),
            content_release_date=request.POST.get("date_release"),
            details_id=details
        )
        return redirect('webadmin:homepage')
        
    return render(request,"Admin/AddContent.html",{
        'Title':content_title
    })


# Add Series
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
        return render(request,'Admin/AddSeries.html',{
            'Details':content_details,
            'msg':msg
        })
    return render(request,'Admin/AddSeries.html',{
        'Details':content_details
    })


# Add Crew Details 
def add_crew_details(request):
    content_details = tbl_content_details.objects.order_by("-id")
    if request.method == 'POST':
        details = tbl_content_details.objects.get(id=request.POST.get("sel_title"))
        tbl_crew.objects.create(
            details_id = details,
            crew_name = request.POST.get("txt_name"),
            crew_photo = request.FILES.get("file_photo"),
            crew_role = request.POST.get("txt_role")
        )
    return render(request,'Admin/AddCrewDetails.html',{
        'Details':content_details
    })

# Add Content Trailer
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
        
        return redirect('webadmin:add_content')
        
    return render(request,'Admin/AddContentTrailer.html',{
        'Content':content_data
    })


# Content Management
# Content Display
def content_display(request):
    content_details = tbl_content_details.objects.filter(details_status = 1).order_by("-id")
    
    return render(request,'Admin/ContentManagement.html',{
        'Details':content_details
    })


# User Content Management 
def user_content_management(request):
    content_details = tbl_content_details.objects.exclude(user_id__isnull=True).filter(details_status=0)
    return render(request,'Admin/UsersContentManagement.html',{
        'Details':content_details
    })

# Accept User Content 
def accept_content(request,aid):
    content = tbl_content_details.objects.get(id=aid)
    content.details_status = 1
    content.save()
    return redirect('webadmin:user_content_manage')

# Reject User Contents 
def reject_content(request,rid):
    content = tbl_content_details.objects.get(id=rid)
    content.details_status = 3
    content.save()
    return redirect('webadmin:user_content_manage')

# Series Details List 
def series_details_list(request,sid):
    series_details = tbl_content.objects.filter(details_id=sid)
    # for i in series_details:
    #     print(i.details_id.id)
    return render(request,'Admin/SeriesList.html',{
        'Series_Details':series_details
    })

# Content Playing in Admin Side
def content_play_in_admin(request,cid):
    # print(cid)
    content = tbl_content.objects.get(details_id=cid)
    content_details = tbl_content_details.objects.get(id=content.details_id.id)
    movie = True
    return render(request,'Admin/ContentPlay.html',{
        'Content_data':content,
        'Details':content_details
    })

# Series Play In Admin 
def series_play_in_admin(request,cid):
    # print(cid)
    content = tbl_content.objects.get(id=cid)
    content_details = tbl_content_details.objects.get(id=content.details_id.id)
    return render(request,'Admin/ContentPlay.html',{
        'Content_data':content,
        'Details':content_details
    })


# View Trailers In Admin
def view_trailer(request,tid):
    data = tbl_trailer.objects.get(details_id=tid)
    link = data.trailer_url
    video_id = extract_video_id(link)
    # print("Video ID:", video_id)
    
    return render(request,'Admin/ViewTrailers.html',{'Trailer':video_id})

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


# View Complaints 
def view_complaints(request):
    complaints = tbl_complaint.objects.filter(complaint_status = 0)
    return render(request,'Admin/ViewComplaints.html',{
        'Complaints':complaints
    })

# Replay Complaints 
def replay_complaint(request,rid):
    complaint = tbl_complaint.objects.get(id=rid)
    if request.method == 'POST':
        data = tbl_complaint.objects.get(id=rid)
        data.complaint_replay = request.POST.get("txt_replay")
        data.complaint_status = 1
        data.save()
        return redirect('webadmin:view_complaints')
    else:
        return render(request,'Admin/ReplayComplaint.html',{
            'Complaint':complaint
        })


# Users list
def users_list(request):
    user=tbl_user.objects.all()
    return render(request,'Admin/UsersList.html',{
        'Users':user
    })

# User Ban
def user_ban(request,uid):
    tbl_user.objects.get(id=uid).delete()
    return redirect('webadmin:users_list')

# Show Feedbacks 
def view_feedbacks(request):
    feedbacks = tbl_feedback.objects.all().order_by('-id')
    return render(request,'Admin/Feedbacks.html',{
        'feedbacks':feedbacks
    })