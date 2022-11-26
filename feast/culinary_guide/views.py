from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage

from .models import Dishes, Categories


def index(request):
    return render(request, 'home.html', {'user': request.user})


def first_meal(request):
    dishes = Dishes.objects.filter(category=1)
    return render(request, 'first_meal.html', {'dishes': dishes})


def main_dishes(request):
    dishes = Dishes.objects.filter(category=2)
    return render(request, 'main_dishes.html', {'dishes': dishes})


def bakery_productsl(request):
    dishes = Dishes.objects.filter(category=3)
    return render(request, 'bakery_productsl.html', {'dishes': dishes})


def add_dish(request):
    categories = Categories.objects.all()
    dishes = Dishes.objects.filter(user=request.user.id)
    return render(request, 'add_dish.html', {'dishes': dishes, 'categories': categories})


def new_dish(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    products = request.POST.get('products')
    recipe = request.POST.get('recipe')
    image = request.FILES['image']
    fss = FileSystemStorage('culinary_guide/static/images')
    saved_file = fss.save(image.name, image)
    category = request.POST.get('select')
    dish = Dishes()
    dish.title = title
    dish.description = description
    dish.products = products
    dish.recipe = recipe
    dish.image = image.name
    dish.category = Categories(category)
    dish.user = User(request.user.id)
    dish.save()
    return HttpResponseRedirect('/add_dish')



def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(name, email, password)
        user.last_name = 'Lennon'
        user.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'registration.html')


def login_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
