from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_user(request):
    print("Getting info from this rat bastard"),
    request.session['first_name'] = request.POST['first_name']
    request.session['locations'] = request.POST['locations']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    # context = {
    #     "first_name": request.POST["first_name"],
    #     "locations": request.POST["locations"],
    #     "language": request.POST["language"],
    #     "comment": request.POST["comment"]
    # }
    return redirect('muthafucka/')

def muthafucka(request):
    print("Got that bastahds info")
    return render(request, "results.html")