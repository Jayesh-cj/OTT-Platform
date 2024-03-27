from django.db import models
from Guest.models import tbl_user
# Create your models here.


# Admin table
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.EmailField()
    admin_password=models.CharField(max_length=10)


# # District Table
# class tbl_district(models.Model):
#     district_name=models.CharField(max_length=50)


# # Place Table
# class tbl_place(models.Model):
#     place_name=models.CharField(max_length=50)
#     district_id=models.ForeignKey(tbl_district,on_delete=models.CASCADE,null=True)


# Language Table
class tbl_language(models.Model):
    language_name=models.CharField(max_length=50)


# Genre Table
class tbl_genre(models.Model):
    genre_name=models.CharField(max_length=50)


# Category Table
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)


# Subscription Package Table
class tbl_package(models.Model):
    package_title=models.CharField(max_length=50)
    package_validity=models.IntegerField()
    package_price=models.IntegerField()
    package_discription=models.TextField()

# Content Details Table
class tbl_content_details(models.Model):
    # trailer_id = models.ForeignKey(tbl_trailer, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(tbl_category, on_delete=models.CASCADE,null=True)
    language_id = models.ForeignKey(tbl_language, on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
    details_certificate = models.CharField(max_length=100)
    details_title = models.CharField(max_length=500)
    details_description = models.TextField()
    details_photo = models.FileField(upload_to='Files/Contents/Posters/')
    # status 1 = Accepted to release 
    # status 2 = Release date passed 
    # status 3 = Rejected 
    details_status = models.IntegerField(default=0)
    details_genres = models.CharField(max_length=50,null=True)
    # Single File = 0
    # Multiple File = 1
    details_filesize = models.IntegerField(default=0)
    

# Content Trailer Table
class tbl_trailer(models.Model):
    details_id = models.ForeignKey(tbl_content_details, on_delete=models.CASCADE, null=True)
    trailer_release_date = models.DateField()
    trailer_url = models.CharField(max_length=600)
    # trailer_duration = models.TimeField()

# Crew Table
class tbl_crew(models.Model):
    details_id = models.ForeignKey(tbl_content_details, on_delete=models.CASCADE, null=True)
    crew_name = models.CharField(max_length=200)
    crew_role = models.CharField(max_length=200)
    crew_photo = models.FileField(upload_to='Files/Contents/Crew/')


# Content Table
class tbl_content(models.Model):
    details_id = models.ForeignKey(tbl_content_details, on_delete=models.CASCADE,null=True)
    content_season = models.IntegerField(null=True)
    content_episode = models.IntegerField(null=True) 
    content_file = models.FileField(upload_to='Files/Contents/')
    content_release_date = models.DateField()
    content_duration = models.CharField(max_length=10)
    content_title = models.CharField(max_length=500)
    content_description = models.TextField()



# Content Genre Table
# class tbl_content_genre(models.Model):
#     details_id = models.ForeignKey(tbl_content_details, on_delete=models.CASCADE, null=True)
#     genre_id = models.ForeignKey(tbl_genre, on_delete=models.CASCADE, null=True)