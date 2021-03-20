from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class BookJournalBase(AbstractUser):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    username = None

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    genre = models.CharField(max_length=255)


class Journal(BookJournalBase):
    publisher = models.CharField(max_length=255)
    # type = models.Choices()
