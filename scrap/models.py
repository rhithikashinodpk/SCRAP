
from django.db import models

from django.contrib.auth.models import User

from datetime import datetime

from django.utils import timezone

from django.db.models.signals import post_save


# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profilepics")
    def __str__(self) -> str:
        return self.user.username

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Scrap(models.Model):
    name=models.CharField(max_length=200)
    condition=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    picture=models.ImageField(upload_to="scrapimages",null=True ,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_scrap")
    place=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="scrap_category")
    created_date=models.DateTimeField(auto_now_add=True)
    status_option=(
        ("sold","sold"),
        ("available","available")
    )
    status=models.CharField(choices=status_option, max_length=200,default="available")
    # user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_scrap")

    def __str__(self):
        return self.name

class WishList(models.Model):
    scrap=models.ManyToManyField(Scrap)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_wishlist")
    created_date=models.DateTimeField(auto_now_add=True)

class Bids(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_bids")
    scrap=models.ForeignKey(Scrap,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    option=(
        ("reject","reject"),
        ("pending","pending"),
        ("accept","accept")
    )
    status=models.CharField(choices=option, max_length=200,default="pending")

    def __str__(self) -> str:
        return self.amount

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_reviews")
    scrap=models.ForeignKey(Scrap,on_delete=models.CASCADE)
    comments=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()

    def __str__(self):
        return self.comments

def create_profile(sender,created,instance,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("Created")

post_save.connect(create_profile,sender=User)
