from django.db import models

# Create your models here.
class Author(models.Model):
    #Author model stores name of an author and can be linked to many books (1-to-many relationship)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title= models.CharField(max_length=255)
    publication_year = models.IntegerField() #must not be a future year (validated in the serializer)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title 