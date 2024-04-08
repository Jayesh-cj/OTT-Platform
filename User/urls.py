from django.urls import path,include
from User import views

app_name = 'webuser'

urlpatterns = [

    path('Homepage/',views.homepage,name="homepage"),

    
    path('MyProfile/',views.show_profie, name="show_profile"),
    path('EditProfile/',views.edit_profile, name="edit_profile"),
    path('ChangePassword/',views.change_password, name="change_password"),

    path('Packages/',views.view_package_deatails,name="package_deatails"),

    path('SubcribePackage/<int:pid>',views.subscribe_package,name="subscribe_package"),
    path('Payment/', views.payment, name='payment'),

    path('Add Genre/',views.add_genre, name="add_genre"),
    path('Add Content Details/',views.add_content_details, name='add_users_contents_details'),
    path('Add Content/',views.add_content, name='add_user_content'),
    path('Add Multiple Files/',views.add_series, name='add_users_series'),
    path('Add Trailer/',views.add_trailer, name='add_content_trailer'),
    # path('Add Crew Details/',views.add_crew_details, name='add_c'),
    path('Conten Status/',views.check_content_ststus, name='check_content_status'),

    path('ContentDetails/<int:cid>',views.content_details, name="content_details"),
    # path('SeriesList/<int:cid>',views.series_episode_list, name="episode_list"),
    path('EpisodeDetails/<int:cid>',views.episode_details, name="episode_details"),
    path('CrewDetails/<int:cid>',views.crew_details, name='crew_details'),
    path('Play Content/<int:pid>',views.play_content, name='play_content'),
    path('ViewTrailer/<int:tid>',views.view_trailer,name="view_trailer"),

    path('AddContentIntoWatchlist/<int:wid>/<int:cid>', views.add_content_in_watchlit, name="add_content_in_watchlist"),
    path('Create Watchlist/',views.create_watchlist, name='create_watchlist'),
    path('View Watchlist Contents/<int:wid>',views.view_watchlist_contents, name="view_watchlist_contents"),
    path('Remove Content From Watchlist/<int:rid>',views.delete_from_watchlist, name='remove_from_watchlist'),

    path('Review Content/',views.review_contents, name="review_content"),
    
    path('Complaints/',views.view_complaints, name='view_complaints'),
    path('Complaint To Admin/',views.complaint_to_admin, name="complaint_to_admin"),

    path('Feedback/',views.feedback, name='feedback'),

    path('rating/<str:cid>',views.rating,name="rating"),
    path('ajaxrating',views.ajaxrating,name="ajaxrating"),
    path('starrating/',views.starrating,name="starrating"),

    path('create chatroom/',views.create_chatroom, name='create_chatroom'),
    path('Chatromms/',views.chatroom_list, name='chatrooms'),
    path('Joined List/',views.joined_chatroom_list, name='joined_list'),
    path('JoinCommunity/<int:jid>',views.join_chatroom, name='join_chatroom'),

    path('chatpage/<int:rid>',views.chatpage,name="chatpage"),
    path('ajaxchat/<int:rid>',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/<int:rid>',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),


    path('All Contents/',views.all_contents_display, name="display_all_contents"),
    path('AjaxSearch/', views.AjaxSearch, name="ajax_search"),
    path('Logout/',views.logout, name="logout"),
]