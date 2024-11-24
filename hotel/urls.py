"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hotel, name="hotel"),
    path('hotel/', views.hotel, name="hotel"),
    path('visitors/<int:id_visitor>', views.visitors, name="visitors"),
    path('search-name/', views.search_name, name="search_name"),
    path('search-year/', views.search_year, name="search_year"),
    path('room/', views.room, name="room"),
    path('passport_form/', views.passport_form, name="passport_form"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
]
