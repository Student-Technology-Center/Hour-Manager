from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from hour_manager.models import PostedShiftModel
from datetime import datetime

from utils.message import send_stc_email

def delete(request, pk):

	try:
		target_shift = PostedShiftModel.objects.get(pk=pk)
	except:
		return JsonResponse({
	        'status':'failed',
	        'message':'Invalid primary key'
	    })

	if request.user == target_shift.posted_by:
		target_shift.delete()

		return JsonResponse({
	        'status':'success',
	        'message':'Shift deleted'
	    })

	else:
		return JsonResponse({
	        'status':'failed',
	        'message':'Current user and shift user do not match'
	    })


@require_http_methods('POST')
def claim(request):
	data = request.POST

	shift_pk = data.get('pk', False)
	start_time = datetime.strptime(data.get('start_time', False), '%I:%M%p').time()
	end_time = datetime.strptime(data.get('end_time', False), '%I:%M%p').time()

	try:
		shift = PostedShiftModel.objects.get(pk=shift_pk)
	except:
		return JsonResponse({
	        'status':'failed',
	        'message':'Invalid primary key'
	    })


	if start_time < shift.start_time or end_time > shift.end_time or start_time >= end_time:
		return JsonResponse({
	        'status':'failed',
	        'message':'Invalid claim times'
	    })

	# Checking time range to split the shift claim
	if start_time == shift.start_time and end_time == shift.end_time:
		shift.taken_by = request.user
		shift.save()

	else:
		if start_time > shift.start_time:
			start_trimmed_shift = PostedShiftModel(
				posted_by = shift.posted_by,
				start_time = shift.start_time,
				end_time = start_time,
				date = shift.date,
				reason = shift.reason)

			start_trimmed_shift.save()

			shift.start_time = start_time
			shift.taken_by = request.user
			shift.save()

		if end_time < shift.end_time:
			end_trimmed_shift = PostedShiftModel(
				posted_by = shift.posted_by,
				start_time = end_time,
				end_time = shift.end_time,
				date = shift.date,
				reason = shift.reason)

			end_trimmed_shift.save()

			shift.end_time = end_time
			shift.taken_by = request.user
			shift.save()

	# Informing the person whose shift was taken
	subject = "{} claimed your hours!".format(request.user.first_name)
	message = """Your shift on {} from {} to {} was claimed by {}!""".format(shift.date, start_time, end_time, request.user.first_name)
	send_stc_email(subject, message, {request.user.email}, True)

	return JsonResponse({
        'status':'success',
        'message':'Shift claimed'
    })