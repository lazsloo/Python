"""camped_app URL Configuration

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
    path('', views.reg_login),
    path('HQ', views.HQ),
    path('host', views.host),
    path('camped', views.camped),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('create', views.camped_create),
    path('HQ/<int:camp_id>/join', views.join),
    path('HQ/<int:camp_id>/leave', views.leave),
    path('profile/<int:user_id>', views.profile),
    path('update_user/<int:user_id>', views.update_user),
    path('camped/<int:camp_id>', views.info),
    path('delete/<int:camp_id>', views.delete),
    path('camped/<int:camp_id>/edit', views.edit),
    path('update_camp/<int:camp_id>', views.update_camp),
]
