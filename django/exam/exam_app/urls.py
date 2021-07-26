"""exam_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('wishes', views.index),
    path('wishes/new', views.wish),
    path('make_a_wish', views.make_a_wish),
    path('delete_wish/<int:wish_id>', views.delete_wish),
    path('wishes/edit/<int:wish_id>', views.edit_wish),
    path('update_wish/edit/<int:wish_id>', views.update_wish),
    path('granted/<int:wish_id>', views.granted),
]