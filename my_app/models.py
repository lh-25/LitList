from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  description = models.TextField()
  
  READ_STATUS_CHOICES = [
    ('P', 'Planned to read'),
    ('R', 'Reading'),
    ('F', 'Finished')
  ]
  read_status = models.CharField(
    max_length=1,
    choices=READ_STATUS_CHOICES,
    default='P',
  )
  publish_date = models.DateField()
  genre = models.CharField(max_length=100)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
      return reverse('book-detail', kwargs={'book_id': self.id})