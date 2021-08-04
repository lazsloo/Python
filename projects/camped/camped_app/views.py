from django.shortcuts import render, redirect

# Create your views here.
def reg_login(request):
    return render(request, 'reg_login.html')