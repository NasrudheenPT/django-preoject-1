from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from django.core.mail import send_mail
from sample import settings

# Create your views here.

def main(request):
    return render(request,'main.html')
@login_required(login_url='/login/')
def insert(request):
    nef=NewStudentForm()
    if request.method=="POST":
        nef=NewStudentForm(request.POST)
        if nef.is_valid():
            nef.save()
            return redirect(insert)
    else:
        return render(request,'insert.html',{'data':nef})
@login_required(login_url='/login/')       
def view(request):
    if request.user.is_authenticated:
        stud=Student.objects.all()
        return render(request,'view.html',{'stu':stud})
    else:
        return redirect(login)
def update_fun(request,id): 
    
    nef=NewStudentForm()
    if request.method=='POST':
        obj=Student.objects.get(pk=id)
        nef=NewStudentForm(request.POST,instance=obj)
        if nef.is_valid():
            nef.save()
            return redirect(view)
        
    else:
        obj=Student.objects.get(pk=id)
        nef=NewStudentForm(instance=obj)
        return render(request,'update.html',{'data':nef})

def delete_fun(request,id):
        obj=Student.objects.get(pk=id)
        obj.delete()
        return redirect(view)


def createuser(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return render(request,"create.html",{'myform':form})
    
    else:
        form = UserCreationForm()
        return render(request,"create.html",{'myform':form})
def login_fn(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,password)
        check = authenticate(request,username=username,password=password)
        if check:
            login(request,check)
            request.session['usertype']='admin'
            return redirect(main)
        else:
            return HttpResponse("NOT A VALID USER")

def logout_fn(request):
    logout(request)
    return redirect(main)


@login_required(login_url='/login/')
def fileupload(request):
    if request.method =='GET':
        form = ImageUploadForm()
        return render(request,'fileupload.html',{'form':form})
    else:
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(main)
        else:
            return render(request,'fileupload.html',{'form':form})
@login_required(login_url='/login/')
def viewfile(request):
    viewfile = img.objects.all()
    return render(request,'viewfile.html',{'data':viewfile})

def emailsend(request):
    send_mail('email sending using python subbb','message from python ',settings.EMAIL_HOST_USER,['idreesakkadan@gmail.com'])





   

        
