from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.forms import model_to_dict

from books.models import Book

def list(request: HttpRequest) -> HttpResponse:

    books = Book.objects.all().order_by('title')

    context = {
        'books': books,               
        'title': 'cписок книг',  
        'total_books': books.count() 
    }

    return render(request, 'books/book_list.html', context)

def book_id_html(request: HttpRequest, book_id) -> HttpResponse:

    book = get_object_or_404(Book, id=book_id)

    context = {
            'book': book,               
            'title': f'Описание книги',  
            }

    return render(request, 'books/book_id.html', context)

def books_json(request: HttpRequest) -> JsonResponse:

    books = Book.objects.all().order_by('title')

    books_data = [model_to_dict(book) for book in books]

    return JsonResponse(books_data, safe=False)

def books_json_id(request: HttpRequest, book_id) -> JsonResponse:

    book = get_object_or_404(Book, id=book_id)

    book_data = model_to_dict(book)

    return JsonResponse(book_data)
