from django.contrib import admin
from django.urls import path 
#import veiws for metods calling 
from home import views


urlpatterns = [
    #declaring the methods name for caliing   
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
]
