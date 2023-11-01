from django.db import models

# Create your models here.
class ShortURL (models.Model) :
    original_URL = models.URLField(max_length=2000)
    short_URL = models.CharField(max_length=200)
    time_date_created = models.DateTimeField()

    def __str__(self) :
        return self.original_URL

