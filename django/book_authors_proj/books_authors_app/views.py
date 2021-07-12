from django.shortcuts import redirect, render
from .models import book, author

# Create your views here.
def index(request):
    context = {
        "books": book.objects.all(),
    }
    return render(request, "index.html", context)

def titles(request):
    if (request.method == "POST"):
        book.objects.create(
            title=request.POST["title"],
            desc=request.POST['desc']
        )
    return redirect("/")

def book_view(request, book_id):
    if {request.method == "GET"}:
        context = {
            "getBook": book.objects.get(id=book_id),
            "authors": author.objects.all(),
        }
        return render(request, "view_author.html", context)

def add_author(request, book_id):
    if (request.method == "POST"):
        thisAuthor = author.objects.get(id=request.POST['author'])
        thisBook = book.objects.get(id=book_id)
        thisBook.authors.add(thisAuthor)
    return redirect(f'/books/{book_id}')