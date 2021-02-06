from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.contrib.sessions.models import Session
from . import models
# Create your views here.
def index(request):
    return render(request,'mainapp/index.html')

def reg(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        specification = request.POST['spc']
        if password==cpassword:
            user = User.objects.create_user(email=email,password=password,first_name=fname,last_name=lname, username=email)
            newuser = models.Userext(specification=specification,user=user)
            newuser.save()
            return redirect('/')
        else:
            messages.error(request, 'Passwords did not match')
            return redirect('/register')
    else:
        return render(request,'mainapp/reg.html')

def workerreg(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['cpass']
        spc = request.POST['spc']
        if password==cpassword:
            user = User.objects.create_user(spc=spc,email=email,password=password,first_name=fname,last_name=lname, username=email)
            user.save()
            return redirect('/')
        else:
            messages.error(request, 'Passwords did not match')
            return redirect('/registerw')
    else:
        return render(request,'mainapp/reg.html')

def log(request):
    if request.session.has_key('logged'):
        return redirect('/')
    if request.method=='POST':
        uname = request.POST['uname']
        password = request.POST['pass']
        user = auth.authenticate(username=uname,password=password)
        if user !=None:
            auth.login(request, user)
            request.session['logged']=True
            checkdetails(request)
            return redirect('/')
        else:
            return render(request, 'mainapp/log.html')
    else:
        return render(request,'mainapp/log.html')

def logout(request):
    request.session['logged'] = False
    auth.logout(request)
    return redirect('/')


def checkdetails(request):
    data= models.Userext.objects.filter(user=request.user)
    return render(request,'mainapp/basic.html',{'data':data})