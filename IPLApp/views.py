from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserModel
import operator

# Create your views here.


def adminloginview(request):
    return render(request, "IPLApp/adminlogin.html")


def authenticate_admin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    # user exists
    if user is not None and user.username == 'admin':
        login(request, user)
        return redirect('adminhomepage')


def admin_homepage_view(request):
    li = UserModel.objects.all()
    ordered = sorted(li, key=operator.attrgetter('points'), reverse=True)
    context = {'thofes': ordered}
    return render(request, 'IPLApp/adminhomepage.html', context)


def logout_admin(request):
    logout(request)
    return redirect('adminloginpage')


def update_points(request):
    name = request.POST['name']
    points = request.POST['points']
    u = UserModel.objects.get(name=name)
    ppoints = int(u.points)
    u.points = ppoints+int(points)
    u.save()
    return redirect('adminhomepage')
