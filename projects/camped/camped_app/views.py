from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User, Camp
import bcrypt

# Create your views here.
def reg_login(request):
        if 'userid' in request.session:
            return redirect('/HQ')
        return render(request, 'reg_login.html')

def HQ(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.all()
    }
    return render(request, "HQ.html", context)

def host(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, "host.html", context)

def info(request, camp_id):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.get(id=camp_id)
    }
    return render(request, "info.html", context)

def edit(request, camp_id):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.get(id=camp_id)
    }
    return render(request, "edit.html", context)

def search(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.all()
    }
    return render(request, "search.html", context)

def profile(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.all()
    }
    return render(request, "profile.html", context)

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
            password=pw_hash,
            )
        messages.success(request, "Registration successful!")
        request.session['userid'] = Users.id
        return redirect("/HQ")
    return redirect("/")

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.error(request, "Sucessfully logged in!")
            return redirect("/HQ")
        else:
            messages.error(request, "Invalid e-mail or password")
    else:
        messages.error(request, "E-mail not found")
    return redirect("/")

def logout(request):
    messages.error(request, "Successfully logged out!")
    request.session.flush()
    return redirect("/")

def camped_create(request):
    errors = Camp.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
    else:
        camp = Camp.objects.create(
            title=request.POST['title'],
            type=request.POST['type'],
            location=request.POST['location'],
            attendee=request.POST['attendee'],
            date=request.POST['date'],
            time=request.POST['time'],
            camped_event=User.objects.get(id=request.session['userid']))
        user = User.objects.get(id=request.session['userid'])
        user.host_camped.add(camp)
        return redirect(f"/camped/{camp.id}")
    return redirect("/host")

def delete(request, camp_id):
    delete_camp = Camp.objects.get(id=camp_id)
    if (request.method=="GET"):
        delete_camp.delete()
    return redirect("/")

def update_camp (request, camp_id):
    errors = Camp.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/edit/{camp_id}")

    if (request.method == "POST"):
        update_camp = Camp.objects.get(id=camp_id)
        update_camp.title = request.POST['title']
        update_camp.type = request.POST['type']
        update_camp.location = request.POST['location']
        update_camp.attendee = request.POST['attendee']
        update_camp.date = request.POST['date']
        update_camp.time = request.POST['time']
        update_camp.save()
        return redirect(f"/camped/{camp_id}")