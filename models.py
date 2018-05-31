'''Used to connecting our hour manager server to the SQL DB'''
from django.db import models
from django.contrib.auth import get_user_model

from  shiftmanager.models import Shift

USER_MODEL = get_user_model()

class HourModel(models.Model):
    user        = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    shifts      = models.ForeignKey(Shift, on_delete=models.CASCADE)
    reason      = models.CharField(max_length=120, default="")

class HourHistoryModel(models.Model):
    claimed_by  = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    shift       = models.OneToOneField(HourModel, on_delete=models.CASCADE)
    claimed_at  = models.DateTimeField(auto_now=True)