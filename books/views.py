from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.forms import model_to_dict

from django.db.models import QuerySet

from books.models import Book
from .forms import BookForm

def list(request: HttpRequest) -> HttpResponse:

    books: QuerySet[Book] = Book.objects.all().order_by('title')

    context = {
        'books': books,               
        'title': 'Cписок книг',  
        'total_books': books.count(),
        'form': BookForm(),
        'open_modal': False,
    }

    return render(request, 'books/book_list.html', context)

def book_id_html(request: HttpRequest, book_id: int) -> HttpResponse:

    book: Book = get_object_or_404(Book, id=book_id)

    context = {
            'book': book,               
            'title': 'Описание книги',  
            }

    return render(request, 'books/book_id.html', context)

def add_book(request: HttpRequest):
    if request.method == "POST":
        form: BookForm = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:list')
        
        books: QuerySet[Book] = Book.objects.all().order_by('title')
        context = {
            'books': books,
            'title': 'Список книг',
            'total_books': books.count(),
            'form': form,
            'open_modal': True,
        }
        return render(request, 'books/book_list.html', context, status=400)
                    
 
    return redirect('books:list')

    



def books_json(request: HttpRequest) -> JsonResponse:

    books = Book.objects.all().order_by('title')

    books_data = [model_to_dict(book) for book in books]

    return JsonResponse(books_data, safe=False)

def book_json_id(request: HttpRequest, book_id: int) -> JsonResponse:

    book = get_object_or_404(Book, id=book_id)

    book_data = model_to_dict(book)

    return JsonResponse(book_data)
