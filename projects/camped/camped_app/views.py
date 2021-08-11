from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User, Camp
from datetime import datetime
import bcrypt

# Create your views here.
def reg_login(request):
        if 'userid' in request.session:
            return redirect('/HQ')
        return render(request, 'reg_login.html')

def HQ(request):
    now = datetime.now()
    context = {
        "date": now.strftime("%Y/%m/%d"),
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.all()
    }
    return render(request, "HQ.html", context)

def host(request):
    z = [
        'Car Camping',
        'Overlanding',
        'Backpacking',
        'Bicycle Camping',
        'Winter Camping',
        'Canone Camping',
        'Rv Camping'
    ]
    x = [
        2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
    ]
    return render(request, 'host.html', {'z': z} | {'x': x})

def info(request, camp_id):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.get(id=camp_id)
    }
    return render(request, "info.html", context)

def edit(request, camp_id):
    z = [
        'Car Camping',
        'Overlanding',
        'Backpacking',
        'Bicycle Camping',
        'Winter Camping',
        'Canone Camping',
        'Rv Camping'
    ]
    x = [
        2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
    ]
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.get(id=camp_id)
    }
    return render(request, "edit.html", context | {'z': z} | {'x': x})

def camped(request):
    now = datetime.now()
    context = {
        "date": now.strftime("%Y/%m/%d"),
        "user": User.objects.get(id=request.session['userid']),
        "camp": Camp.objects.all()
    }
    return render(request, "camped.html", context)

def profile(request, user_id):
    context = {
        "user": User.objects.get(id=user_id),
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
        users = User.objects.create(
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'], 
            email=request.POST['email'], 
            password=pw_hash,
            )
        messages.success(request, "Registration successful!")
        request.session['userid'] = users.id
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
        user.user_joined.add(camp)
        messages.error(request, "Camped event successfully created")
        return redirect(f"/camped/{camp.id}")
    return redirect("/host")

def join(request, camp_id):
    joined = Camp.objects.get(id=camp_id)
    user = User.objects.get(id=request.session['userid'])
    joined.camped_join.add(user)
    messages.error(request, "Joined Camped event")
    return redirect('/HQ')

def leave(request, camp_id):
    leave = Camp.objects.get(id=camp_id)
    user = User.objects.get(id=request.session['userid'])
    leave.camped_join.remove(user)
    messages.error(request, "Left Camped event")
    return redirect('/HQ')


def delete(request, camp_id):
    delete_camp = Camp.objects.get(id=camp_id)
    if (request.method=="GET"):
        delete_camp.delete()
        messages.error(request, "Camped event successfully deleted")
    return redirect("/")

def update_camp (request, camp_id):
    errors = Camp.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/camped/{camp_id}/edit")
    if (request.method == "POST"):
        update_camp = Camp.objects.get(id=camp_id)
        update_camp.title = request.POST['title']
        update_camp.type = request.POST['type']
        update_camp.location = request.POST['location']
        update_camp.attendee = request.POST['attendee']
        update_camp.date = request.POST['date']
        update_camp.time = request.POST['time']
        update_camp.save()
        messages.error(request, "Camped event successfully updated")
        return redirect(f"/camped/{camp_id}")

def update_user (request, user_id):
    errors = User.objects.update_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f"/profile/{user_id}")
    if (request.method == "POST"):
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash)
        update_user = User.objects.get(id=user_id)
        update_user.first_name = request.POST['first_name']
        update_user.last_name = request.POST['last_name']
        update_user.email = request.POST['email']
        update_user.password = password=pw_hash
        update_user.save()
        messages.error(request, "User profile updated")
        return redirect(f"/profile/{user_id}")

