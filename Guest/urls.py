from django.urls import path,include
from Guest import views

app_name = 'webguest'

urlpatterns = [

    path('',views.landing_page, name='landig_page'),

    path('UserRegistration/',views.user_registration,name="user_registration"),

    path('Login/',views.user_login,name="user_login"),

]