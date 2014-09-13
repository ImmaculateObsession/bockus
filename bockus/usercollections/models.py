from django.db import models
from django.contrib.auth.models import User

from books.models import Book, Cover

# Create your models here.
class UserBook(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    cover = models.ForeignKey(Cover)
    rating = models.PositiveSmallIntegerField(max_length=5)

class Tag(models.Model):
    name = models.CharField(max_length=25)

    # create intermediary manytomany table
    # https://docs.djangoproject.com/en/dev/topics/db/models/#intermediary-manytomany
    books = models.ManyToManyField(UserBook, through="TaggedUserBook")

    # self referencing ManyToMany stack-overflow question
    # http://stackoverflow.com/questions/3880489/how-do-i-write-a-django-model-with-manytomany-relationsship-with-self-through-a
    groups = models.ManyToManyField('self', through="TagGroup", symmetrical=False)


class TaggedUserBook(models.Model):
    userBook = models.ForeignKey(UserBook)
    tag = models.ForeignKey(Tag)
    order_in_tag_list = models.PositiveIntegerField()

class TagGroup(models.Model):
    parent = models.ForeignKey(Tag, related_name='parent')
    child = models.ForeignKey(Tag, related_name='child')
    order_in_parent_list = models.PositiveIntegerField()