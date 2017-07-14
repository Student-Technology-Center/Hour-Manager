'''Hour manager sub directory views stored here'''
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from hour_manager.models import HourModel, hour_history

@login_required
def hour(request, pk):
    hour = HourModel.objects.get(pk=pk)
    return JsonResponse(
        {
            "username":hour.username,
            "first_name":hour.first_name,
            "last_name":hour.last_name,
            "date":hour.date.isoformat(),
            "start_time":hour.start_time.strftime('%H:%M'),
            "end_time":hour.end_time.strftime('%H:%M'),
            "reason":hour.reason,
        }
    )