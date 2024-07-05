from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


# Create your views here.

def display_book(request):
    book_list = Book.objects.all()
    context = {'book_list':book_list}
    return render(request, 'book_list.html', context)

def add_book(request):  
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        print("GAGAL")
    return render(request, 'add_book.html', {'form':form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)
   
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form':form})


def delete_book(request, book_id):
    book = get_object_or_404(Book, id = book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book':book})
    