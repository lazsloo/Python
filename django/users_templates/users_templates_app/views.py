from django.shortcuts import redirect, render
from .models import user

# Create your views here.
def index(request):
    context = {
        "users": user.objects.all(),
    }
    return render(request, "index.html", context)

def users(request):
    if (request.method == "POST"):
        user.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            age=request.POST['age']
        )
    return redirect("/")

def edit(request, user_id):
    if (request.method == "GET"):
        context = {
            "user": user.objects.get(id=user_id)
        }
        return render(request, "edit_user.html", context)
    if (request.method == "POST"):
        new_user = user.objects.get(id=user_id)
        new_user.name = request.POST['name']
        new_user.email = request.POST['email']
        new_user.age = int(request.POST['age'])
        new_user.save()
        return redirect("/")