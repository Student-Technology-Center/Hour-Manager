from django.db import models
from django.contrib.auth import get_user_model

from shiftmanager.models import Shift


try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except:
    from django.contrib.auth.models import User

USER_MODEL = User

#USER_MODEL = get_user_model()



class HourModel(models.Model):
    user        = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    shifts      = models.ForeignKey(Shift, on_delete=models.CASCADE)
    reason      = models.CharField(max_length=120, default="")

class HourHistoryModel(models.Model):
    claimed_by  = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    shift       = models.OneToOneField(HourModel, on_delete=models.CASCADE)
    claimed_at  = models.DateTimeField(auto_now=True)
