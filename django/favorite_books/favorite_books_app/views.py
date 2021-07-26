from django.shortcuts import render, redirect
from django.contrib import messages
from . models import User, Books
import bcrypt

# Create your views here.
def index(request):
    if 'userid' in request.session:
        return redirect('/books')
    return render(request, "index.html")

def register(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)

    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()   
        print(pw_hash)

        Users = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        messages.success(request, "Registration successful!")
        request.session['userid'] = Users.id

        return redirect("/books")
    return redirect("/")

def login(request):

    users = User.objects.filter(email=request.POST['email'])

    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.success(request, "Login successful!")
            return redirect("/books")
        else:
            messages.error(request, "Invalid e-mail or password")
    else:
        messages.error(request, "E-mail not found")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def user(request):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "books": Books.objects.all()
    }
    return render(request, "user.html", context)

def add_book(request):
    errors = Books.objects.validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request, val)
    else:
        books = Books.objects.create(title=request.POST['title'], desc=request.POST['desc'], uploaded_by_id=User.objects.get(id=request.session['userid']))
######################################################################
        user = User.objects.get(id=request.session['userid'])
        user.liked_books.add(books)
# This will add to your favorites when you create a book 
######################################################################
    return redirect('/books')

def info(request, book_id):
    context = {
        "user": User.objects.get(id=request.session['userid']),
        "book": Books.objects.get(id=book_id)
    }
    return render(request, "info.html", context)

def like(request, book_id):
    book = Books.objects.get(id=book_id)
    user = User.objects.get(id=request.session['userid'])
    book.users_who_liked.add(user)
    return redirect('/books')

def unlike(request, book_id):
    book = Books.objects.get(id=book_id)
    user = User.objects.get(id=request.session['userid'])
    book.users_who_liked.remove(user)
    return redirect('/books')

def edit(request):
    context = {
    "user": User.objects.get(id=request.session['userid'])
    }
    return render(request, 'edit.html')


def update_book (request, book_id):
    errors = Books.objects.validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')

    if (request.method == "POST"):
        update = Books.objects.get(id=book_id)
        update.title = request.POST['title']
        update.desc = request.POST['desc']
        update.save()
    return redirect('/shows')