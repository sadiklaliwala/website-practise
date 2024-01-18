#import the httpresponse for the return to the website 
from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import About
# Create your views here.
#defining the methods for show datw
def home(request):
    context={"variable1":20}
    return render(request,"main.html",context)
    #return HttpResponse("this is the hoem page ")

def about(request):
   if request.method=="POST":
       name= request.POST.get('name')
       contact= request.POST.get('phone')
       email= request.POST.get('email')
       date=datetime.today()
       pro = About(name = name, contact = contact , email = email, date = date)
       pro.save()
   return render(request , "about.html") 
def contact(request):
    return render(request , "contact.html")
def services(request):
    return render(request , "services.html")