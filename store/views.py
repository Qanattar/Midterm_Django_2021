
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *


# Create your views here.


@api_view(['GET'])
def book_items(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def insert_book_item(request: HttpRequest):
    book = Book(content=request.POST['content'])
    book.save()
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['GET'])
def delete_book_item(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    serializer = BookSerializer(book_to_delete)
    return Response(serializer.data)


@api_view(['GET'])
def journal_items(request):
    journals = Journal.objects.all()
    serializer = JournalSerializer(journals, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def insert_journal_item(request: HttpRequest):
    journal = Journal(content=request.POST['content'])
    journal.save()
    serializer = JournalSerializer(journal)
    return Response(serializer.data)


@api_view(['GET'])
def delete_journal_item(request, journal_id):
    journal_to_delete = Journal.objects.get(id=journal_id)
    journal_to_delete.delete()
    serializer = JournalSerializer(journal_to_delete)
    return Response(serializer.data)
