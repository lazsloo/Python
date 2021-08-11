from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now()
    context = {
        "time": now.strftime("%Y-%m-%d %H:%M %p")
    }
    return render(request,'index.html', context)