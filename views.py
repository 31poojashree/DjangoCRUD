from django.shortcuts import render , redirect
from .models import Student

# Create your views here.
def home(request):
    std = Student.objects.all()
    return render(request, "home.html", {'std':std})

def navbar(request):
    return render(request, "navbar.html")

def delete(request,roll):
    s = Student.objects.get(pk=roll)
    s.delete()
    return redirect("/home/")

def update(request,roll):
    std = Student.objects.get(pk=roll)
    return render(request,"update.html" ,{'std':std})
   

def add(request):
    if request.method == 'POST':
        #retrives the user inputs
        st_roll = request.POST.get("std_roll")
        st_name = request.POST.get("std_name")
        st_email = request.POST.get("std_email")
        st_address = request.POST.get("std_address")
        st_phone = request.POST.get("std_phone")
        
        # create models objects
        s=Student()
        s.roll=st_roll
        s.name=st_name
        s.email=st_email
        s.address=st_address
        s.phone=st_phone
        s.save()
        return redirect("/home/")
        
    return render(request, "add.html")

def do_update(request,roll):
        #retrives the user inputs
        st_roll = request.POST.get("std_roll")
        st_name = request.POST.get("std_name")
        st_email = request.POST.get("std_email")
        st_address = request.POST.get("std_address")
        st_phone = request.POST.get("std_phone")
        
        # create models objects
        std = Student.objects.get(pk=roll)
        
        std.roll=st_roll
        std.name=st_name
        std.email=st_email
        std.address=st_address
        std.phone=st_phone
        std.save()
        return redirect("/home/")
   
    