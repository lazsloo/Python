"""the_wall_app URL Configuration

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
    path('', views.index),
    path('create', views.create_user),
    path('login', views.login),
    path('registration', views.registration),
    path('logout', views.logout),
    path('wall', views.wall),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('message/<int:message_id>/post_comment', views.post_comment),
    path('user/<int:user_id>', views.user),
    path('message/<int:message_id>/like', views.like),
    path('message/<int:message_id>/unlike', views.unlike),
]
