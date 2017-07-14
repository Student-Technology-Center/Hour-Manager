'''Hour manager sub directory views stored here'''
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from hour_manager.models import HourModel, hour_history

import json

@login_required
def hour(request, pk):
    hour = HourModel.objects.get(pk=pk)
    print(hour.start_time.strftime('%I:%M %p') if hour.start_time.strftime('%I:%M %p')[0] != "0" else hour.start_time.strftime('%I:%M %p')[1:])
    return JsonResponse(
        {
            "pk":hour.pk,
            "username":hour.username,
            "first_name":hour.first_name,
            "last_name":hour.last_name,
            "date":hour.date.strftime('%B %d, %Y'),
            "start_time":hour.start_time.strftime('%I:%M %p') if hour.start_time.strftime('%I:%M %p')[0] != "0" else hour.start_time.strftime('%I:%M %p')[1:],
            "end_time":hour.end_time.strftime('%I:%M %p') if hour.end_time.strftime('%I:%M %p')[0] != "0" else hour.end_time.strftime('%I:%M %p')[1:],
            "reason":hour.reason,
        }
    )

@login_required
def all_hours(request):
    hours = HourModel.objects.all()
    json_hours = [
            {
                "username":hour.username,
                "first_name":hour.first_name,
                "last_name":hour.last_name,
                "date":hour.date.strftime('%B %d, %Y') ,
                "start_time":hour.start_time.strftime('%I:%M %p') if hour.start_time.strftime('%I:%M %p')[0] != "0" else hour.start_time.strftime('%I:%M %p')[1:],
                "end_time":hour.end_time.strftime('%I:%M %p') if hour.end_time.strftime('%I:%M %p')[0] != "0" else hour.end_time.strftime('%I:%M %p')[1:],
                "reason":hour.reason,
            }
            for hour in hours
        ]
    
    return JsonResponse(json_hours, safe=False)