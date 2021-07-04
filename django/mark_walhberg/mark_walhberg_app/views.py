# other imports
from django.shortcuts import render
from .models import Book
# show all of the data from a table
def index(request):
    context = {
    	"Books": Book.objects.all(),
    }
    return render(request,"index.html", context)