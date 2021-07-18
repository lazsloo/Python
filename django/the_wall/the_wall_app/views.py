from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User, Message, Comment
import bcrypt

# Create your views here.
def index(request):
    if 'userid' in request.session:
        return redirect('/wall')
    return render(request, "index.html")

def create_user(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)

    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash)

        Users = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        messages.success(request, "Registration successful!")
        request.session['userid'] = Users.id

        return redirect("/registration")
    return redirect("/")

def registration(request):
    context = {
        "Users": User.objects.get(id=request.session['userid'])
    }
    return render(request, "login_successful.html", context)

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.success(request, "Login successful!")
            return redirect("/registration")
        else:
            messages.error(request, "Invalid Email/Password combo bruh")
    else:
        messages.error(request, "Account not found with e-mail bruh")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def wall(request):
    context = {
        "Users": User.objects.get(id=request.session['userid']),
        "All_messages": Message.objects.all()
    }
    return render(request, "wall.html", context)

########################################################
def post_message(request):
    errors = Message.objects.validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
    else:
        Messages = Message.objects.create(content=request.POST['content'], creator=User.objects.get(id=request.session['userid']))
    return redirect('/wall')
# This method is for posting messages with a validator to check message length
########################################################

def post_comment(request, message_id):
    errors = Comment.objects.validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
    else:
        Messages = Comment.objects.create(content=request.POST['content'], creator=User.objects.get(id=request.session['userid']), message=Message.objects.get(id=message_id))
    return redirect('/wall')