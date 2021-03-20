from django.urls import path

from . import views


urlpatterns = [
    path('books/', views.book_items),
    path('journals/', views.journal_items),
    path('books/delete/<int:book_id>', views.delete_book_item),
    path('journals/delete/<int:journal_id>', views.delete_journal_item),
    path('books/insert/', views.insert_book_item),
    path('journals/insert/', views.insert_journal_item),
]
