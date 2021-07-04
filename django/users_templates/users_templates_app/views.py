from django.shortcuts import redirect, render
from .models import user

# Create your views here.
def index(request):
    context = {
        "users": user.objects.all(),
    }
    return render(request, "index.html", context)

def add(request):
    if (request.method == "POST"):
        user.objects.create(name=request.POST['name'], email=request.POST['email'], age=request.POST['age'])
    return redirect("/")