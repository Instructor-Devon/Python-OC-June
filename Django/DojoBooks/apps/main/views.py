from django.shortcuts import render, redirect
from .models import Book
# Create your views here.

# show all books
def index(request):
    # if GET show books
    if request.method == "GET":
        context = {
            "books": Book.objects.all()
        }
        return render(request, 'main/books.html', context)
    elif request.method == "POST":
    # if POST create book
    # validations could go here or in models.py
        Book.objects.create(title=request.POST['title'])
    return redirect('/book')

# show one book
def show_book(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id)
    }
    return render(request, 'main/show_book.html', context)

# create a book
def create_book(request):
    # request.POST
    if request.method == "POST":
        # validations could go here or in models.py
        Book.objects.create(title=request.POST['title'])
    return redirect('/book')

# update a book
def update_book(request, book_id):
    if request.method == 'POST':
        # get the object
        book = Book.objects.get(id=book_id)
        # update the fields
        book.title = request.POST['title']
        # save it
        book.save()
    return redirect("/book")

# delete a book
def delete_book(request, book_id):
     # get the object
    book = Book.objects.get(id=book_id)
    # kill it
    book.delete()
    return redirect('/book')