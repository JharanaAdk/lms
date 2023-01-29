from django.shortcuts import render, redirect

from . forms import *
from . models import *

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def book(request):
    book = Book.objects.all() 
    context = {'book':book}
    return render(request, 'book/index.html', context)

def createbook(request):
    if request.method =="GET":
        book_form = BookForm
        return render(request, 'book/add_book.html', context={'form': book_form})
    else:
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            return redirect('book')  
    return render(request, 'book/add_book.html', context={'form': book_form})

def editbook(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(instance=book)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit_book.html', {'form': form})

def readbook(request, book_id):
    book = Book.objects.get(id = book_id)
    context = {'book': book}
    return render(request, 'book/view_book.html', context)

def deletebook(request, book_id):
    book = Book.objects.get(id= book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book')
    else:
        return render(request, 'book/delete_book.html', {'book':book})













# def editbook(request, book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'book/edit_book.html', {'form': form})

















