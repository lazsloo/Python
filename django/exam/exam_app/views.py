from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User, Wish
import bcrypt

# Create your views here.
def login_page(request):
    if 'userid' in request.session:
        return redirect('/wishes')
    return render(request, "login_page.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash)
        Users = User.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'], 
            password=pw_hash
            )
        messages.success(request, "Registration successful!")
        request.session['userid'] = Users.id
        return redirect("/wishes")
    return redirect("/")

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.success(request, "Login successful!")
            return redirect("/wishes")
        else:
            messages.error(request, "Invalid e-mail or password")
    else:
        messages.error(request, "E-mail not found")
    return redirect('/')

def logout(request):
    messages.error(request, "Successfully logged out")
    request.session.flush()
    return redirect('/')

def index(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "wishes": Wish.objects.all(),
    }
    return render(request, "index.html", context)

def wish(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, "make_a_wish.html", context)

def make_a_wish(request):
    errors = Wish.objects.validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/wishes/new')
    else:
        wish = Wish.objects.create(
            title=request.POST['title'], 
            desc=request.POST['desc'], 
            uploaded_by_id=User.objects.get(id=request.session['userid'])
            )
    return redirect('/wishes')

def delete_wish(request, wish_id):
    wish_delete = Wish.objects.get(id=wish_id)
    if (request.method=="GET"):
        wish_delete.delete()
    return redirect("/wishes")

def edit_wish(request, wish_id):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "wish": Wish.objects.get(id=wish_id)
    }
    return render(request, "edit_wish.html", context)

def update_wish (request, wish_id):
    errors = Wish.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/wishes/edit/{wish_id}")

    if (request.method == "POST"):
        update_wish = Wish.objects.get(id=wish_id)
        update_wish.title = request.POST['title']
        update_wish.desc = request.POST['desc']
        update_wish.save()
        return redirect("/wishes")

def granted(request, wish_id):
        wish_granted = Wish.objects.get(id=wish_id)
        if wish_granted.granted_wish is False:
            wish_granted.granted_wish = True
            wish_granted.save()
        return redirect("/wishes")