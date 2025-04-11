
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# CREATE - Add a new book
def add_book(request):
    """
    View to add a new book to the library.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()
    
    return render(request, 'library/book_form.html', {'form': form})

# READ - List all books
def book_list(request):
    """
    View to display all books in the library.
    """
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

# UPDATE - Edit book details
def edit_book(request, book_id):
    """
    View to edit an existing book's details.
    """
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'library/book_form.html', {'form': form})

# DELETE - Remove a book
def delete_book(request, book_id):
    """
    View to delete a book from the library.
    """
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    
    return render(request, 'library/book_confirm_delete.html', {'book': book})
