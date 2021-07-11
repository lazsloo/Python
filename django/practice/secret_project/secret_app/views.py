from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import user

# Create your views here.
def index(request):
    context = {
        "users": user.objects.all()
    }
    return render(request,"index.html",context)

def rat_bastahd(request):
    if (request.method == "POST"):
        user.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],age=request.POST['age'])
    return redirect("/")