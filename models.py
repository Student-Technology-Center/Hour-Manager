from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except:
    from django.contrib.auth.models import User

USER = User

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

OPEN_HOURS = {
	0 : '8:00AM',
	1 : '9:00AM',
	2 : '10:00AM',
	3 : '11:00AM',
	4 : '12:00PM',
	5 : '1:00PM',
	6 : '2:00PM',
	7 : '3:00PM',
	8 : '4:00PM',
	9 : '5:00PM',
	10 : '6:00PM',
	11 : '7:00PM',
	12 : '8:00PM',
	13 : '9:00PM',
}


class ShiftModel(models.Model):
	user        = models.ForeignKey(USER, on_delete=models.CASCADE)
	start_time  = models.TimeField()
	end_time 	= models.TimeField()
	day 		= models.CharField(max_length=1, choices=DAYS_OF_WEEK)

class PostedShiftModel(models.Model):
	posted_by 	= models.ForeignKey(USER, on_delete=models.CASCADE, related_name='posted_by')
	taken_by	= models.ForeignKey(USER, on_delete=models.CASCADE, null=True, related_name='taken_by')
	start_time  = models.TimeField()
	end_time    = models.TimeField()
	date 		= models.DateField()
	reason      = models.CharField(max_length=300, blank=True)
