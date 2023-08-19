from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def signup(request):
   if request.method=="POST":
     get_email=request.POST.get('email')
     get_password=request.POST.get('password')
     get_conformation=request.POST.get('confirmation')
    
     if get_password!=get_conformation:
        messages.info(request,'password is not matching')
        return redirect('/auth/signup/')
     try:
        if User.objects.get(username=get_email):
           messages.warning(request,"email is taken")
     except Exception as identifier:
        pass
     myuser=User.objects.create_user(get_email,get_email,get_password)
     myuser.save()
     messages.success(request,'user is created')
     return redirect('/auth/signin/')


   return render(request, 'signup.html')

def signin(request):
    if request.method=="POST":
       get_email=request.POST.get('email')
       get_password=request.POST.get('password')
       myuser=authenticate(username=get_email, password=get_password)
       if myuser is not None:
          login(request,myuser)
          messages.success(request,"login success")
          return redirect('/Bio/home/')
       else:
          messages.error(request,"invalid credentials")
          

    return render(request, 'login.html')


def signout(request):
   logout(request)
   messages.success(request,"logout successfully")
   return redirect('/auth/signin/')