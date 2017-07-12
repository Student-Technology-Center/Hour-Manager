'''Used to connecting our hour manager server to the SQL DB'''
from django.db import models

# Create your models here.
class HourModel(models.Model):
    '''A model for holding hours'''
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    reason = models.CharField(max_length=120)

    def __str__(self):
        '''Returns a string representation of the entry'''
        return "{} {} | {}:{}".format(self.first_name, self.last_name, self.date, self.start_time)

class hour_history(models.Model):
    cover_username = models.CharField(max_length=25)
    coveree_first = models.CharField(max_length=15)
    coveree_last = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()