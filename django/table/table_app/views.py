from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User, Wish
import bcrypt

# Create your views here.
def index(request):
    if 'userid' in request.session:
        return redirect('/wish')
    return render(request, "index.html")

def register(request):
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
        return redirect("/wish")
    return redirect("/")

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.success(request, "Login successful!")
            return redirect("/wish")
        else:
            messages.error(request, "Invalid e-mail or password")
    else:
        messages.error(request, "E-mail not found")
    return redirect('/')

def logout(request):
    messages.error(request, "Successfully logged out")
    request.session.flush()
    return redirect('/')

def delete_wish(request):
    wish_delete = Wish.objects.get(id=request.session['userid'])
    if (request.method=="GET"):
        wish_delete.delete()
    return redirect("/wish")

def wish_page(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "wishes": Wish.objects.all()
    }
    return render(request, "wish.html", context)

def add_wish(request):
    errors = Wish.objects.validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
    else:
        wish = Wish.objects.create(title=request.POST['title'], desc=request.POST['desc'], uploaded_by_id=User.objects.get(id=request.session['userid']))
    return redirect('/wish')

def view_wish(request, wish_id):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "wish": Wish.objects.get(id=wish_id)
    }
    return render(request, "view_wish.html", context)

def grant_wish(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    user = User.objects.get(id=request.session['userid'])
    wish.users_who_granted.add(user)
    return redirect('/wish')