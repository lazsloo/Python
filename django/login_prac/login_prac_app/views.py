from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    context = {
        "Users": User.objects.all()
    }
    return render(request, "index.html", context)

def create_user_form(request):
    return render(request, "create_user_form.html")

def create_user(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/new/user')

    if (request.method == 'POST'):
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/")

def delete_user(request, user_id):
    delete_user = User.objects.get(id=user_id)
    if (request.method == "GET"):
        delete_user.delete()
    return redirect("/")

def edit_user_form(request, user_id):
    if (request.method == "GET"):
        context = {
            "Users": User.objects.get(id=user_id)
        }
    return render(request, "update_user_form.html", context)

def edit_user(request, user_id):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/user/{user_id}/edit')

    if (request.method == "POST"):
        update_user = User.objects.get(id=user_id)
        update_user.first_name = request.POST['first_name']
        update_user.last_name = request.POST['last_name']
        update_user.email = request.POST['email']
        update_user.save()
    return redirect("/")

def view_user(request, user_id):
    context = {
        "Users": User.objects.get(id=user_id)
    }
    return render(request, "user_info.html", context)