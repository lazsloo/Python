from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):

    return render(request, "index.html")

def create(request):
    errors = User.objects.user_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)

    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash)

        Users = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], username=request.POST['username'], password=pw_hash)

        request.session['userid'] = Users.id
        messages.success(request, "Weeb has been born!")
        return redirect('/')
    return redirect('/')

def login_page(request):
    context = {
        "Users": User.objects.get(id=request.session['userid'])
    }
    return render(request, "user_login.html", context)

def login(request):
    users = User.objects.filter(username=request.POST['username'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect("/login_page")
        else:
            messages.error(request, "Invalid password for your Isekei")
    else:
        messages.error(request, "You're still a pleb, there's no Isekei registered")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')