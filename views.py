from django.shortcuts import render
from django.http import HttpResponseRedirect
from hour_manager.forms import PostShiftForm
from hour_manager.models import OPEN_HOURS, PostedShiftModel
from utils.message import send_stc_email

from django.contrib.auth.decorators import login_required, permission_required
from login.decorators import user_is_email_confirmed
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from pandas import date_range
import datetime

# Importing the User model according to Alex
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except:
    from django.contrib.auth.models import User

USER = User


@login_required
@user_is_email_confirmed
def index(request):

	available_shifts = PostedShiftModel.objects.filter(taken_by__isnull=True).order_by('date')

	shifts = dict()
	for shift in available_shifts:
		hour_range = date_range(start=shift.start_time.strftime("%I:%M%p"), end=shift.end_time.strftime("%I:%M%p"), freq='H')
		shifts[shift] = [time.strftime("%I:%M%p").lstrip('0') for time in hour_range]

	context = {
		'hours' : OPEN_HOURS.values(),
		'shifts' : shifts,
	}
	return render(	
		request,
		'hourmanager_index.html',
		context
	)

@login_required
@user_is_email_confirmed
def post(request):

	# Hours were just posted
	if request.method == 'POST':
		form = PostShiftForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data

			start_time=data.get('start_time')
			end_time=data.get('end_time')
			date=data.get('date')
			reason=data.get('reason')

			new_shift = PostedShiftModel.objects.create(
				posted_by=request.user,
				start_time=start_time,
				end_time=end_time,
				date=date,
				reason=reason
				)

			subject = "New hours"
			message = \
				"{} {} has just put hours up on the hour manager!\n\nFrom {} to {} on {}\n\nBecause: {}" \
					.format(
						request.user.first_name, 
						request.user.last_name, 
						start_time.strftime('%I:%M %p'),
						end_time.strftime('%I:%M %p'), 
						date, 
						reason)

			user_emails = [x.email for x in USER.objects.all()]

			send_stc_email(subject, message, user_emails, True)

			return HttpResponseRedirect('/hourmanager/')

	# No posted hours
	else:
		form = PostShiftForm()


	context = {
		'hours' : OPEN_HOURS.values(),
		'form' : form,
	}

	return render(
		request,
		'hourmanager_post.html',
		context
	)

@login_required
@user_is_email_confirmed
def history(request):

	covered_shifts = PostedShiftModel.objects.exclude(taken_by__isnull=True).order_by('-date', 'start_time')

	context = {
		'shifts' : covered_shifts,
	}

	return render(
		request,
		'hourmanager_history.html',
		context
	)