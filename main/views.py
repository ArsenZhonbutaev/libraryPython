from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo

def homepage(request):
    book_list = ToDo.objects.all()
    return render(request, "index.html", {"book_list": book_list})

def add_book(request):
    form = request.POST
    title = form["book_title"]
    price = form["book_price"]
    author = form["book_author"]
    genre = form["book_genre"]
    year = form["book_year"]
    description = form["book_description"]
    book = ToDo(
        title=title, 
        price=price,
        author=author,
        genre=genre,
        year=year,
        description=description
        )
    book.save()
    return redirect("home")

    """ price = form["book_price"]
    book = ToDo(price=price)
    author = form["book_author"]
    book = ToDo(author=author)
    genre = form["book_genre"]
    book = ToDo(genre=genre)
    year = form["book_year"]
    book = ToDo(year=year)
    description = form["book_description"]
    book = ToDo(description=description) """