from django.urls import path,include
from Admin import views

app_name = 'webadmin'

urlpatterns = [
    path('Homepage/',views.homepage,name='homepage'),

    path('ChangePassword/',views.change_password, name="change_password"),

    # path('District/',views.district,name='district'),
    # path('Del_district/<int:did>',views.del_district,name='del_district'),
    # path('Edit_district/<int:eid>',views.edit_district,name="edit_district"),
    
    # path('Place/',views.place,name='place'),
    # path('Del_place/<int:did>',views.del_place,name='del_place'),
    # path('Edit_place/<int:eid>',views.edit_place,name='edit_place'),

    path('Category/',views.category,name='category'),
    path('Del_Category/<int:cid>',views.del_category,name="del_category"),
    path('Edit_Category/<int:eid>',views.edit_category,name="edit_category"),

    path('Language/',views.language,name="language"),
    path('Edit_Language/<int:eid>',views.edit_language,name="edit_language"),
    path('Del_Language/<int:did>',views.del_language,name="del_language"),

    path('Genre/',views.genre,name="genre"),
    path('Edit_Genre/<int:eid>',views.edit_genre,name="edit_genre"),
    path('Del_Genre/<int:did>',views.del_genre,name="del_genre"),

    path('Package/',views.package,name="package"),
    path('Edit_Package/<int:eid>',views.edit_package,name="edit_package"),
    path('Del_Package/<int:did>',views.del_package,name="del_package"),

    path('AddContentDetails/',views.add_content_details,name="add_content_details"),
    path('AddContent/',views.add_content,name="add_content"),
    path('AddSeries/',views.add_series, name="add_series"),
    path('AddCrewDetails/',views.add_crew_details, name='add_crew_details') ,
    path('AddContentTrailer/',views.add_trailer, name="upload_trailer"),

    path('ContentManagement/',views.content_display, name="content_display"),
    path('User Content Management/',views.user_content_management, name="user_content_manage"),
    path('AcceptContent/<int:aid>',views.accept_content, name='accept_content'),
    path('RejectContent/<int:rid>',views.reject_content, name='reject_content'),
    path('SeriesDetailsList/<int:sid>',views.series_details_list, name="series_details"),
    path('ContentPlay/<int:cid>',views.content_play_in_admin, name="content_play"),
    path('SeriesPlay/<int:cid>',views.series_play_in_admin, name="series_play"),

    path('ViewTrailer/<int:tid>',views.view_trailer,name="view_trailer"),

    path('VieewComplaints/',views.view_complaints, name="view_complaints"),
    path('ReplayComplaint/<int:rid>',views.replay_complaint, name="replay_complaint"),

    path('UsersList/',views.users_list,name="users_list"),
    path('BanUser/<int:uid>',views.user_ban,name="user_ban"),
    path('Feedbacks/',views.view_feedbacks,name="feedbacks"),

]