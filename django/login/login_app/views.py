from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def login_page(request):
    return render( request, "login_page.html")

def create_user(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)

#################################################################
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash) # encrypts the password

        Users = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
#################################################################

        request.session['userid'] = Users.id

        return redirect("/user/registration")
    return redirect("/")

#################################################################
def registration(request):
    context = {
        "Users": User.objects.get(id=request.session['userid'])
    }
    return render(request, "login_successful.html", context)
# Instead of "get" we use reuqest.session['<variable>'] when we're using a login
#################################################################

#################################################################################### 
def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect("/user/registration")
        else:
            messages.error(request, "Invalid Email/Password combo bruh")
    else:
        messages.error(request, "Account not found with e-mail bruh")
    return redirect("/")
# This is for the login to a site w/ urls
####################################################################################

########################### 
def logout(request):
    request.session.flush()
    return redirect('/')
# Logout w/ urls built in
###########################