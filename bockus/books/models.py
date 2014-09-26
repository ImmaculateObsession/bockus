from django.db import models


COVER_TYPE_CHOICES = (
    ("Front", "Front"),
    ("Spine", "Spine"),
    ("Back", "Back"),
    ("Full", "Full - Front, Spine & Back"),
)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author_first_name = models.CharField(max_length=100)
    author_last_name = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.title + " by " + self.author_last_name + ", " + self.author_first_name

class Cover(models.Model):
    book = models.ForeignKey(Book)
    publisher = models.CharField(max_length=25)
    publish_date = models.DateField()
    # image = models.ImageField(upload_to="book_covers")
    type = models.CharField(max_length=10, choices=COVER_TYPE_CHOICES)

    def __str__(self):
        return self.type + " - " + self.book.title + " by " + \
            self.book.author_last_name + ", " + self.book.author_first_name

