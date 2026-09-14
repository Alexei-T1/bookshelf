from django.urls import path
from . import views

app_name = 'books'  

urlpatterns = [
    # html-представление всех книг в виде таблицы
    path('books/', views.list, name='list'),
    
    # html-представление книги id
    path('book/<int:book_id>/', views.book_id_html, name='book_id_html'),


  
    # json-представление всех книг
    path('api/books/', views.books_json, name='books_json'),

    # json-представление книги id
        path('api/book/<int:book_id>/', views.book_json_id, name='book_json_id'),
]