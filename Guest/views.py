from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *

# Create your views here.


# Index Page 
def landing_page(request):
    return render(request,'Guest/Index.html')


# User Registration
def user_registration(request):
    if request.method=='POST' and request.FILES:
        password = request.POST.get("txt_password")
        con_password = request.POST.get("txt_con_password")
        print(password)
        print(con_password)
        if password == con_password:
            tbl_user.objects.create(
                user_name=request.POST.get("txt_name"),
                user_contact=request.POST.get("num_contact"),
                user_email=request.POST.get("txt_email"),
                user_photo=request.FILES.get("file_photo"),
                user_gender=request.POST.get("gender"),
                user_dob=request.POST.get("date_dob"),
                user_password=request.POST.get("txt_password")
            )
            return redirect('webguest:landig_page')
        else:
            msg = "Password Missmatch!"
            return render(request,'Guest/UserRegistration.html',{
                'msg':msg
            })
    else:
        return render(request,'Guest/UserRegistration.html')


# Login
def user_login(request):
    if request.method=="POST":
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")

        u_count = tbl_user.objects.filter(user_email=email,user_password=password).count()
        a_count = tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        
        if u_count > 0:
            user = tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"]=user.id
            return redirect('webuser:homepage')
        elif a_count > 0:
            admin = tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"]=admin.id
            return redirect('webadmin:homepage')
        else:
            msg = "Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'msg':msg })
    return render(request,'Guest/Login.html')

