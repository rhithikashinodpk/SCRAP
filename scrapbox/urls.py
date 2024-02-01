"""
URL configuration for scrapbox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from scrap import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.RegistrationView.as_view(),name="register"),
    path('signin',views.LoginView.as_view(),name="signin"),
    path('index',views.IndexView.as_view(),name="index"),
    path('scrap/signout',views.LogoutView.as_view(),name="signout"),    
    path('scrapadd',views.ScrapAddView.as_view(),name="scrapadd"),
    path('scrapdetail/<int:pk>/detail/',views.ScrapDetailView.as_view(),name="scrapdetails"),
    path('scrapupdate/<int:pk>/change/',views.ScrapUpdateView.as_view(),name="scrapupdate"),
    path('category',views.CategoryAddView.as_view(),name="category"),
    path('scrapdelete/<int:pk>/remove',views.ScrapDeleteView.as_view(),name="delete"),
    path('scraplist',views.ScrapListView.as_view(),name="scraplist"),
    path('reviews',views.ReviewView.as_view(),name="review"),
    path("profileedit/<int:pk>/change",views.ProfileUpdateView.as_view(),name="profileedit"),
    path("profiledetail/<int:pk>/detail",views.ProfileDetailView.as_view(),name="profiledetail"),
    path("wishlistadd/<int:pk>/wishlist",views.WishlistAddView.as_view(),name='wishlistadd'),
    path("wishlist",views.WishlistView.as_view(),name="wishlist"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)