from django.db import models

from Admin.models import tbl_content_details, tbl_package
from Guest.models import tbl_user

# Create your models here.

# User table

# Admin model import


# Subscription Table
class tbl_subscription(models.Model):
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    package_id = models.ForeignKey(tbl_package, on_delete=models.CASCADE,null=True)
    subscription_date=models.DateField()
    subscription_status=models.IntegerField(default=0)


# Community Table
class tbl_chatroom(models.Model):
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    community_name = models.CharField(max_length=200)
    community_date = models.DateField()
    community_photo = models.FileField(upload_to='Files/Community/Profile/')
    community_description = models.TextField()
    # Open Community = 0
    # Closed Community = 1
    community_status = models.IntegerField(default=0)

# Join list Table
class tbl_joinlist(models.Model):
    community_id = models.ForeignKey(tbl_chatroom, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    list_status = models.IntegerField(default=0)


# # Chat Table
# class tbl_chat(models.Model):
#     community_id = models.ForeignKey(tbl_community, on_delete=models.CASCADE, null=True)
#     user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
#     chat_content = models.TextField()
#     chat_date = models.DateField()

# # Complaint In Community Table
# class tbl_community_complaint(models.Model):
#     user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
#     community_id = models.ForeignKey(tbl_community, on_delete=models.CASCADE, null=True)
#     cmp_community_title = models.CharField(max_length=200)
#     cmp_community_content = models.TextField()
#     cmp_community_date = models.DateField()
#     cmp_community_status = models.IntegerField(default=0)
#     cmp_community_replay = models.TextField()


# Complaint To Admin
class tbl_complaint(models.Model):
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    complaint_title = models.CharField(max_length=200)
    complaint_content = models.TextField()
    complaint_date = models.DateField()
    complaint_status = models.IntegerField(default=0)
    complaint_replay = models.TextField()

# Feedback Table
class tbl_feedback(models.Model):
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    feedback_content = models.TextField()
    feedback_date = models.DateField()


# Watchlist Tables
class tbl_watchlist(models.Model):
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    watchlist_name = models.CharField(max_length=200)

# Watchlist Content Table
class tbL_watchlist_content(models.Model):
    watchlist_id = models.ForeignKey(tbl_watchlist, on_delete=models.CASCADE, null=True)
    details_id = models.ForeignKey(tbl_content_details, on_delete=models.CASCADE, null=True)
    wlist_date = models.DateField()

# Review Table
class tbl_review(models.Model):
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE, null=True)
    details_id = models.ForeignKey(tbl_content_details, on_delete=models.CASCADE, null=True)
    user_rating=models.IntegerField()
    user_review=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    review_datetime=models.DateTimeField(auto_now_add=True)


class tbl_chat(models.Model):
    chat_content=models.CharField(max_length=100)
    chat_file=models.FileField(upload_to='ChatFiles/')
    chat_time=models.DateTimeField()
    user_from=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    room_id = models.ForeignKey(tbl_chatroom, on_delete=models.CASCADE,null=True)
