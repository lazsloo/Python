from django.shortcuts import render, redirect
from .models import dojo, ninja

# Create your views here.
def index(request):
    context = {
        "dojos": dojo.objects.all(),
        "ninjas": ninja.objects.all()
    }
    return render(request, "index.html", context)

def add_dojo(request):
    if (request.method == "POST"):
        dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state']
        )
    return redirect("/")

def add_ninja(request):
    if (request.method == "POST"):
        ninja.objects.create(
            dojo=dojo.objects.get(id=request.POST['dojo']),
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
        )
    return redirect("/")

def delete(request, dojo_id):
    dojoDelete = dojo.objects.get(id=dojo_id)
    if (request.method=="POST"):
        dojoDelete.delete()
    return redirect("/")