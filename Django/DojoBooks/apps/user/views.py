from django.shortcuts import render, redirect
from .models import User
from apps.main.models import Book
# Create your views here.

# show all Users
def root(request):
    return redirect("/book")
def index(request):
    # if GET show Users
    if request.method == "GET":
        context = {
            "users": User.objects.all(),
        }
        return render(request, 'user/users.html', context)
    elif request.method == "POST":
    # if POST create User
    # validations could go here or in models.py
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect('/user')

# show one User
def show_user(request, user_id):
    context = {
        "user": User.objects.get(id=user_id),
        "unfaved": Book.objects.exclude(favs__id=user_id)
    }
    return render(request, 'user/show_user.html', context)


# update a User
def update_user(request, user_id):
    if request.method == 'POST':
        # get the object
        user = User.objects.get(id=user_id)
        # update the fields
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        # save it
        user.save()
    return redirect("/user")

# delete a User
def delete_user(request, user_id):
     # get the object
    user = User.objects.get(id=user_id)
    # kill it
    user.delete()
    return redirect('/user')

def favorite(request, user_id):
    if request.method == "POST":
        # query for a book
        book = Book.objects.get(id = request.POST['book_id'])
        # query for a user
        user = User.objects.get(id=user_id)
        # add book to user's favs
        user.faved_books.add(book)
    return redirect('/')