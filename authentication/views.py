from django.shortcuts import render
from django.http import HttpResponse
from djnago.contrib.auth.models import USER

# Create your views here.
def home(request):
    return HttpResponse("hELLO G")

def signup(request):

    if request.method == 'POST':
        #username1 = request.POST.get('username')      #name attribute of html is used   
        username = request.POST['username']    
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']



    


    return render(request,"authentication/signup.html")

def signin(request):
    return render(request,"authentication/signin.html")

def signout(request):
    pass

def index(request):
    return render(request,"authentication/index.html")
