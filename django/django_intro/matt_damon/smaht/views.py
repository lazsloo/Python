from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "Matt Damon",
        "whateverIWant": "ya brah i'm not sober",
        "languages": ["Python", "Java", "Potato"]
    }
    return render(request, "index.html", context)
    