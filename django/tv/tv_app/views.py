from django.shortcuts import render, redirect
from django.contrib import messages
from .models import show

# Create your views here.
def new_show(request):
    return render(request, "new_show.html")

def create_show(request):

    errors = show.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/shows/new')

    if(request.method == 'POST'):
        newShow = show.objects.create(title=request.POST['title'], network=request.POST['network'], release=request.POST['release'], desc=request.POST['desc'])
    return redirect(f'/shows/{newShow.id}')

def view_show(request, tv_id):
    context = {
        "tvShow": show.objects.get(id=tv_id)
    }
    return render(request, "show_information.html", context)


def all_shows(request):
    context = {
        "shows": show.objects.all()
    }
    return render(request, "shows.html", context)

def get_show (request, update_id):
    if (request.method == "GET"):
        context = {
            "updateShow": show.objects.get(id=update_id)
        }
        return render(request, "update.html", context)

def update_show (request, update_id):
    errors = show.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/shows/{update_id}/edit')

    if (request.method == "POST"):
        update_show = show.objects.get(id=update_id)
        update_show.title = request.POST['title']
        update_show.network = request.POST['network']
        update_show.release = request.POST['release']
        update_show.desc = request.POST['desc']
        update_show.save()
        return redirect(f'/shows/{update_id}')

def delete_show(request, delete_id):
    showDelete = show.objects.get(id=delete_id)
    if (request.method=="GET"):
        showDelete.delete()
    return redirect(f'/shows/')
