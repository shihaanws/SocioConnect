from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.info(request,'You are logged in')
            return redirect('login')
        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('login')    
    else:
        return render(request,'login.html')


def register(request):

    if request.method=='POST':
        username= request.POST['username']
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return   redirect('register')
        return  redirect('/')


    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')     