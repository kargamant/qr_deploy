from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django import forms
from .models import Book


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(label="Имя пользователя", widget = forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
	password = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label="Имя пользователя", widget = forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
	password1 = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label="Подтверждение пароля", widget = forms.PasswordInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label="e-mail", widget = forms.EmailInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'link', 'photo']
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'link': forms.TextInput(attrs={'class':'form-control'})
		}

class ScanForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['qr']