from django.shortcuts import render,redirect
from django.views.generic import View,ListView,CreateView,UpdateView,DetailView,TemplateView
from scrap.models import Scrap,UserProfile,Category,Reviews,Bids,WishList
from scrap.forms import UserForm,LoginForm,ScrapForm,UserProfileForm,CategoryForm,ReviewsForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from scrap.decorator import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

decs=[login_required,never_cache]
# Create your views here.
class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=UserForm
        return render(request,"register.html",{form:"form"})
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("account created")
            return redirect("register")
        else:
            return render(request,"register.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm 
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")     
            pwd=form.cleaned_data.get("password") 

            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("valid")
                
                return redirect("index")
            print("invalid")
            return render(request,"login.html",{"form":form})

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
@method_decorator(decs,name="dispatch")  
class IndexView(ListView):
    template_name="index.html"
    form_class=ScrapForm
    model=Scrap
    context_object_name="data"
           


@method_decorator(decs,name="dispatch")  
class ScrapAddView(CreateView):
    template_name="scrapadd.html"
    form_class=ScrapForm
    model=Scrap

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")

@method_decorator(decs,name="dispatch")  

class ScrapDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Scrap.objects.get(id=id).delete()
        return redirect("index") 
@method_decorator(decs,name="dispatch")  
class ScrapUpdateView(UpdateView):
    template_name="scrapupdate.html"
    form_class=ScrapForm
    model=Scrap

    def get_success_url(self):
        return reverse("index") 
    
@method_decorator(decs,name="dispatch")      
class ScrapListView(ListView):
    template_name="index.html"
    model=Scrap
    context_object_name="data"

@method_decorator(decs,name="dispatch")    
class ScrapDetailView(DetailView):
    template_name="scrapdetail.html"
    model=Scrap 
    context_object_name="data" 

@method_decorator(decs,name="dispatch")  
class ProfileUpdateView(UpdateView):
    template_name="profileedit.html"
    form_class=UserProfileForm
    model=UserProfile
    def get_success_url(self):
         return reverse("index")
    
@method_decorator(decs,name="dispatch")     
class ProfileDetailView(DetailView): 
    template_name="profiledetail.html"
    model=UserProfile 
    context_object_name="data"

@method_decorator(decs,name="dispatch")     
class CategoryAddView(CreateView):
    template_name="category.html"
    form_class=CategoryForm
    model=Category
    
    def get_success_url(self):
        return reverse("index")
    
@method_decorator(decs,name="dispatch")         
class ReviewView(CreateView):
    template_name="scrapdetails.html"
    form_class=ReviewsForm
    model=Reviews

    def get_success_url(self):
        return reverse("scrapdetails")
    
@method_decorator(decs,name="dispatch")        
class WishlistAddView(View):
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        scrap_obj=Scrap.objects.get(id=id)
        action=request.POST.get("action")
        print(action)
        wishlist, created = WishList.objects.get_or_create(user=request.user)
        if action == "add":
            wishlist.scrap.add(scrap_obj)
        elif action == "remove":
            wishlist.scrap.remove(scrap_obj)
            print("removed")
        return redirect("index")
    
@method_decorator(decs,name="dispatch")         
class WishlistView(View):
    def get(self,request,*args,**kwargs):
        qs=WishList.objects.get(user_id=request.user.id)
        wishitems=Scrap.objects.exclude(user=request.user)
        return render(request,"wishlist.html",{"data":qs,"items":wishitems})

    







    


    



# Create your views here.
