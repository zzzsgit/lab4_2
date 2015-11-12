from django.db import models

# Create your models here.
class Book(models.Model):
    ISBN = models.CharField(primary_key = True,max_length = 70)
    Title = models.CharField(max_length = 70)
    AuthorID = models.IntegerField(max_length = 70)
    Publisher = models.CharField(max_length = 70)
    PublishDate = models.DateField(max_length = 70)
    Price = models.CharField(max_length = 70)
    
    def __unicode__(self):
        return self.Title

class Author(models.Model):
    AuthorID = models.IntegerField(primary_key = True,max_length = 70)
    Name = models.CharField(max_length = 70)
    Country = models.CharField(max_length = 70)
    Age = models.CharField(max_length = 70)
    
    def __unicode__(self):
        return self.Name

