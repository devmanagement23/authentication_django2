from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return HttpResponse("hELLO G")

def signup(request):

    if request.method == 'POST':
        #username1 = request.POST.get('username')    # here name attribute of html is used   
        username = request.POST['username']    
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

<<<<<<< HEAD
        # make User  object and enter these values to it
        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        # inbuilt message library of django
        messages.success(request,"Your Account has been successfully created.")

        return redirect('signin')
=======
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
>>>>>>> b4d6fcac844e1eab46e0cebe5cab71f7c2c3e572

        myuser.save()

        messages.success(request,"Your Account has been successfully created")

        return redirect('signin')    

        #below line act like ELSE PART of IF-ELSE   condition
    return render(request,"authentication/signup.html")

def signin(request):
    return render(request,"authentication/signin.html")

def signout(request):
    pass

def index(request):
    return render(request,"authentication/index.html")
