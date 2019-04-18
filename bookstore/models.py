from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_photos',null=True,blank=True)
    bio = models.CharField(max_length=200)
    contact=models.CharField(max_length=12)
    books = models.ForeignKey('Book',on_delete=models.CASCADE,null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    def __str__(self):
        return self.user.username


class Book(models.Model):
    book_title = models.CharField(max_length=40)
    book_description = HTMLField()
    book_image = models.ImageField(upload_to='book')
    live_site = models.URLField(max_length=250)
    book_category = models.CharField(max_length=40, null=True)
    price= models.CharField(max_length=10, null= True)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def save_book(self):
        self.save()

    def delete_book(self):
        self.delete()
        
    def __str__(self):
        return self.book_title