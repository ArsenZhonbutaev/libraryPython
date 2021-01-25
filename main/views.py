from django.shortcuts import render, HttpResponse
from .models import ToDo

def homepage(request):
    book_list = ToDo.objects.all()
    return render(request, "index.html", {"book_list": book_list})
