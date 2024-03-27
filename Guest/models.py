from django.db import models

# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=100)
    user_contact=models.CharField(max_length=15)
    user_email=models.EmailField()
    user_photo=models.FileField(upload_to='Files/User/Profile')
    user_gender=models.CharField(max_length=50)
    user_dob=models.DateField()
    user_password=models.CharField(max_length=10)
