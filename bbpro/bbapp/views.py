from django.shortcuts import render
from .models import * 
# Create your views here.

def index(request):
    return render(request,'bbapp/index.html')

def about(request):
    return render(request,'bbapp/about.html')

def login(request):
    return render(request,'bbapp/login.html')

def register(request):
    return render(request,'bbapp/register.html')

def register_user(request):
    try:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        print("------------>username ",username)
        print("------------>email ",email)
        print("------------>password ",password)
        u_id=User.objects.filter(email=email)
        if u_id:
            e_msg="User already exist"
            return render(request,"bbapp/register.html",{'e_msg':e_msg})
        else:
            if password==repassword:
                uid=User.objects.create(username=username,email=email,password=password)
                if uid:
                    s_msg="successfully added "
                    return render(request,"bbapp/register.html",{'s_msg':s_msg})
                else:
                    e_msg="Invalid Entry "
                    return render(request,"bbapp/register.html")
            else:
                e_msg="password does not match "
                return render(request,"bbapp/register.html",{'e_msg':e_msg})
            
    except:
        e_msg="Invalid Entry"
        return render(request,"bbapp/register.html",{'e_msg':e_msg})

def login_user(request):
    return render(request,"bbapp/login.html")