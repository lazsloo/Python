from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_user(request):
    context = {
        "first_name": request.POST["first_name"],
        "locations": request.POST["locations"],
        "language": request.POST["language"],
        "comment": request.POST["comment"]
    }
    return render(request, "results.html", context)