from django.contrib import admin
from .models import Book

def reg(mod):
    return admin.site.register(mod)

reg(Book)
