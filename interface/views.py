from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserLoginForm, BookForm, ScanForm
from django.contrib.auth import login, logout
import time
import pyqrcode
from .models import Book
from pyzbar.pyzbar import decode
from PIL import Image
import webbrowser
import os

app = 'interface/'
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ScanForm(request.POST, request.FILES)
        if form.is_valid():
            d = decode(Image.open(form.cleaned_data['qr']))
            return redirect(d[0].data.decode('ascii'))
    else:
        form = ScanForm()
        messages.error(request, 'возникла ошибка')
    return render(request, f'{app}index.html', {'form': form})

def books(request):
    return render(request, f'{app}books.html', {'Book': Book})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы зарегистрированы!')
            time.sleep(3)
            return redirect('login')
        else:
            messages.error(request, 'Произошла ошибка при регистрации')
    else:
        form = UserCreationForm()
    return render(request, f'{app}register.html', {'form': form})

def User_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/yourlib')
    else:
        form = UserLoginForm()
    return render(request, f'{app}lonin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            qr = pyqrcode.create(form.cleaned_data['link'])
            dirname = os.getcwd()
            image = f'static/qr_codes/qr_code_{form.cleaned_data["title"]}.png'
            qr.png(image, scale=8)

            photo = form.cleaned_data['photo']
            title = form.cleaned_data['title']
            link = form.cleaned_data['link']
            Book.objects.create(title=title, link=link, photo=photo, qr=image)
            return render(request, f'{app}qr.html', {'image': image})
        else:
            messages.error(request, 'Ошибка')
    else:
        form = BookForm()
    return render(request, f'{app}add_book.html', {'form':form})

def lib(request):
    book_items = Book.objects.all()
    return render(request, f'{app}personal_lib.html', {'book_items': book_items})