from django.shortcuts import render, HttpResponse
from portfolioapp.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    return(render(request, "index.html"))
    # return(HttpResponse("This is homepage"))

def about(request):
    return(render(request, "about.html"))
    # return(HttpResponse("This is about page"))

def project(request):
    return(render(request, "project.html"))
    # return(HttpResponse("This is project page"))

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact = Contact(name= name, email= email, desc= desc, date= datetime.today())
        contact.save()

        messages.success(request, "Your message has been successfully sent!")


    return (render(request, "contact.html"))
    # return(HttpResponse("This is contact page"))


