"""tv_app URL Configuration

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
    path('', views.all_shows),
    path('shows/', views.all_shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:tv_id>', views.view_show),
    path('shows/<int:update_id>/edit', views.update_show),
    path('shows/<int:delete_id>/destroy', views.delete_show)
]
