from django.shortcuts import render,redirect
from .models import Product,category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import registerForm





def home(request):
    
    prodects = Product.objects.all()
    responce = render(request, 'home.html', {'prodects': prodects, })
  
    return responce 

def categorys(request, foo):
    # replace hyphen with space
    foo = foo.replace('-', ' ')
    try:
        category_obj = category.objects.get(name=foo)
        products = Product.objects.filter(category=category_obj)
        return render(request, 'category.html', {'category': category_obj, 'products': products})
    except category.DoesNotExist:
        messages.success(request, 'Your category does not exist.')
        return redirect('home')
        




def  about(request):
    return render(request , 'about.html', {})


def  login_user(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username =username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, ('you have been logged in.....'))
            return redirect('home')
        else:
            messages.success(request, ('There was an error. please try again...'))
            return redirect('login')

    return render(request , 'login.html', {})


def  logout_user(request):
     logout(request)
     messages.success(request,("you have been logged out....."))
     return redirect('home')


def register_user(request):
    form = registerForm()
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate( username = username , password = password)
            login(request, user)
            messages.success(request, ('you have registered'))
            return redirect('home')
        else:
            messages.success(request, ('Whoops!.... there was a problem please try agine....'))
            return redirect('register')
            
    return render(request, 'register.html', {'form':form})


def admin(request):
    return render(request, ) 

def products(request, pk):
    product = Product.objects.get(id= pk)
    return render(request, 'product.html', {'product':product})
