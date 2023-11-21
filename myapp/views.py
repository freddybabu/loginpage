from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'myapp/index.html')


def signup(request):
    
    if request.method == 'POST':
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username=username):
            messages.error(request, 'username is already exist !')
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "email is already registered !")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "username is too long !")
            
        if password1 != password2:
            messages.error(request, "password mismatch !")
        
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "your account has been successfully created ")
        
        return redirect('signin')
        
    return render(request, 'myapp/signup.html')


def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'myapp/index.html', {'fname': fname})
        else:
            messages.error(request, "bad credentials")
            return redirect('home')
            
    return render(request, 'myapp/signin.html')


def signout(request):
    logout(request)
    messages.success(request, "you are successfully logged out !")
    return redirect('home')

