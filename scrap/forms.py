from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scrap.models import Scrap,Category,Reviews,Bids,UserProfile



class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class LoginForm(forms.Form):  
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)

class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scrap
        exclude=("status","user")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=["user"]
   
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"

class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Reviews
        fields="__all__"  

