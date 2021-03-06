from hashlib import sha256
from django.db import models


class Publisher(models.Model):
    # implicit id
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


def author_directory_path(instance, filename):
    *_, extension = filename.split(".")
    fnamehash = sha256(filename.encode("utf-8")).hexdigest()[-10:]
    return f"authors/{fnamehash}.{extension}"


class Author(models.Model):
    # implicit id
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    photo = models.ImageField(upload_to=author_directory_path)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    # implicit id
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
