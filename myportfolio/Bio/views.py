from django.shortcuts import render ,redirect
from django.http import HttpResponse
from Bio.models import reachme,blog,msg
from django.contrib import messages
def base(request):
    return render(request,'base.html')

def home(request):
     if request.method=="POST":
         user_Name=request.POST.get('name')
         user_Email=request.POST.get('email')
         user_Subject=request.POST.get('subject')
         user_message=request.POST.get('message')
         userquery=msg(name=user_Name,email=user_Email,subject=user_Subject,mssages=user_message)
         userquery.save()
         
         

     return render(request,'backup.html')

     
def contact(request):
    if request.method=="POST":
        user_name=request.POST.get('Name')
        lastname=request.POST.get('lastname')
        user_email=request.POST.get('email')
        user_mobile=request.POST.get('mobile')
        user_review=request.POST.get('Discription')
        person=reachme( name=user_name,
            last_name=lastname,
            email=user_email,
            mobile=user_mobile,
            discription= user_review)
        person.save()

        messages.success(request,"your query have been submited , we will contact you soon!!! ")
        
        return redirect('/Bio/home/')
        
    return render(request, 'contact.html')


def blogs(request):
    posts=blog.objects.all()
    context={"posts":posts}
    return render(request,'blogs.html',context)