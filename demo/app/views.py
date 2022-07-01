
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.core.exceptions import ValidationError
from users.forms import CustomUserCreationForm
from django.db.models import Count, Q

from django.views.decorators.csrf import csrf_exempt

from . models import *

def index(request):
    flats = Estate.objects.order_by('-id')
    category = Category.objects.all()   
    return render(request, 'pages/index.html', {'flats':flats, 'category':category})


def about(request):
    return render(request, 'pages/about.html')


# def filter(request):
#     if request.method == 'GET' and 'search' in request.GET:
#         query = request.GET.get('search')
#         estates = Estate.objects.filter(
#             Q(title__icontains=query)
#         )


def all_estates(request):
    estates = Estate.objects.all()
    return render(request, 'pages/Estates.html', {'estates':estates})


def category(request):
    categories = Category.objects.all()
    return render(request, 'app/category.html', {'categories':categories})


def category_detail(request, id):
    categories = Category.objects.all()
    category = Category.objects.get(id = id)
    return render(request, 'pages/category-detail.html', {'category':category, 'categories':categories})




def product_detail(request, id):

    flat = Estate.objects.get(id=id)
    categories = Category.objects.all()
    if request.user.is_authenticated:
        if not View.objects.filter(user=request.user).filter(product=flat).exists():
            view = View()
            view.product = flat
            view.user = request.user
            view.save()

    return render(request, 'pages/product-detail.html', {'flat':flat, 'categories':categories})


def user_index(request):
    return render(request, 'pages/user/index.html')



def personal(request):
    return render(request, 'pages/user/personal.html')



def favourite(request):
    if request.user.is_authenticated:
        user = request.user
        favourites = user.user_favourites.all()
        return render(request, 'pages/user/favourite.html',{'favourites':favourites})
    else:
        return redirect('index')




def sign_in(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
      
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            message = 'Такого пользователя не существует.'   
            return HttpResponse(message)
           
    else:
        return render(request, 'pages/sign_in.html')


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


def sign_up(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            # messages.success(request, 'Account created successfully')
            return redirect('index')
        else:
            messages = ValidationError(list(form.errors.values()))
            return render(request, 'pages/sign_up.html', {'form':form, 'messages':messages})
           
    else:
        form = CustomUserCreationForm()
        return render(request, 'pages/sign_up.html', {'form':form})




def moveEditPersonal(request):
    return render (request, 'pages/user/edit-personal.html')



def editPersonal(request):
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            user = request.user
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            
            number = request.POST.get('number')
            user.first_name = firstname
            user.last_name = lastname
            user.number = number
        
            user.save()
            return render(request, 'pages/user/personal.html')
        else:
            return render(request, 'pages/user/personal.html')
  

    else:
        return render("ok")




@csrf_exempt
def add_favourite(request):
    if request.method == "POST":
        flatId = request.POST.get('flatId')
        user = request.user
        flat = Estate.objects.get(id=flatId)
        if Favourite.objects.filter(user=user).filter(flat = flat).exists():
            favourite = Favourite.objects.filter(user=user).get(flat = flat)         
            favourite.delete()
            flat.is_favourite=False   
            flat.save()  
            return HttpResponse('deleted')
        else:

            favourite = Favourite()
            favourite.user = user
            favourite.flat = flat
            favourite.save()
            flat.is_favourite=True  
            flat.save()         


            return HttpResponse('ok')