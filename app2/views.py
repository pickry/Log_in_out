from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method == 'GET':        
        return render(request, 'signup.html')
    else:
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        pswd = request.POST['password']
        #the argument for create user is lhs for fields in pgadmin in authuser table and rhs is the corresponding variable above
        x = User.objects.create_user(username= username, first_name = fname, last_name = lname, email = email, password = pswd)
        x.save()
        print('user created!')
        return redirect('/')

def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        pswd = request.POST['password']
        user = auth.authenticate(username = username1, password = pswd)
        if user is None:
            messages.error(request,'username or password not correct')
            return redirect('login')
        else:
            auth.login(request, user)
            messages.success(request, "YAY! login successfull")
            return redirect('/')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "logged out")
    return redirect('/')