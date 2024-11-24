from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import Room, PassportForm
from datetime import datetime
from django.contrib.auth import authenticate, login, logout


def hotel(req):
    hotel_ = Hotel.objects.get()
    return render(req, 'hotel_info.html', {"hotel": hotel_})


def visitors(req, id_visitor):
    visitor = Visitor.objects.get(id=id_visitor)
    return render(req, 'visitor_info.html', {"vis": visitor})


def search_name(req):
    query = req.GET.get("q")
    if query:
        passports = Passport.objects.filter(last_name__icontains=query)
    else:
        passports = Passport.objects.all()

    return render(req, "visitors.html", {"passports": passports})


def search_year(req):
    query = req.GET.get("q")
    if query:
        visitors = Visitor.objects.filter(date__year=query)
    else:
        visitors = Visitor.objects.all()

    return render(req, "search_year.html", {"visitors": visitors})


def room(req):
    if req.method == "POST":
        form = Room(req.POST)
    else:
        form = Room()

    return render(req, "room.html", {"form": form})


@login_required
def passport_form(req):
    if req.method == "POST":
        form = PassportForm(req.POST)
        if form.is_valid():
            form.save()
            p = Passport.objects.get(id=len(Passport.objects.all()))
            v = Visitor(name=f"{p.name} {p.last_name}", date=datetime.now(),
                        hotel=Hotel.objects.get(), passport=p)
            v.save()
    else:
        form = PassportForm()

    return render(req, "passport.html", {"form": form})


def user_login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(req, username=username, password=password)
        print(user)
        if user:
            login(req, user=user)
            return redirect("passport_form")

    return render(req, 'login.html')


@login_required
def user_logout(req):
    if req.method == "POST":
        logout(req)
        return redirect("login")
    else:
        return render(req, "logout.html")
