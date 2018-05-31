'''Hour manager sub directory views stored here'''
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from hour_manager.models import HourModel

from . api_helpers import hour_get, hour_post, hour_put, hour_delete

@login_required
def hour(request, pk):
    print(request.method)

    if request.POST:
        hour_post(request, pk)

    if request.GET:
        hour_get(request, pk)

    # if request.PUT:
    #     hour_put(request, pk)

    # if request.DELETE:
    #     hour_delete(request, pk)

    return JsonResponse({
        "failed" : "REST call not supported."
    })

# def spec_hour(request, pk):
#     try:
#         hour = HourModel.objects.get(pk=pk) 
#     except HourModel.DoesNotExist:
#         return JsonResponse(
#             {
#                 "status":"failed",
#                 "message":"This hour does not exist."
#             }
#         )
#     return JsonResponse(
#         {
#             "username":hour.username,
#             "first_name":hour.first_name,
#             "last_name":hour.last_name,
#             "date":hour.date.strftime('%B %d, %Y'),
#             "start_time":hour.start_time.strftime('%I:%M %p') if hour.start_time.strftime('%I:%M %p')[0] != "0" else hour.start_time.strftime('%I:%M %p')[1:],
#             "end_time":hour.end_time.strftime('%I:%M %p') if hour.end_time.strftime('%I:%M %p')[0] != "0" else hour.end_time.strftime('%I:%M %p')[1:],
#             "reason":hour.reason,
#         }
#     )

# @login_required
# def all_hours(request):
#     hours = HourModel.objects.all()
#     json_hours = [
#             {
#                 "username":hour.username,
#                 "first_name":hour.first_name,
#                 "last_name":hour.last_name,
#                 "date":hour.date.strftime('%B %d, %Y') ,
#                 "start_time":hour.start_time.strftime('%I:%M %p') if hour.start_time.strftime('%I:%M %p')[0] != "0" else hour.start_time.strftime('%I:%M %p')[1:],
#                 "end_time":hour.end_time.strftime('%I:%M %p') if hour.end_time.strftime('%I:%M %p')[0] != "0" else hour.end_time.strftime('%I:%M %p')[1:],
#                 "reason":hour.reason,
#             }
#             for hour in hours
#         ]
    
#     return JsonResponse(json_hours, safe=False)