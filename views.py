from django.shortcuts import render
from django.http import HttpResponseRedirect
from hour_manager.forms import PostShiftForm
from hour_manager.models import OPEN_HOURS, PostedShiftModel

from django.contrib.auth.decorators import login_required, permission_required
from login.decorators import user_is_email_confirmed

from pandas import date_range


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
		'hourmanager_index2.html',
		context
	)

@login_required
@user_is_email_confirmed
def post(request):

	if request.method == 'POST':
		form = PostShiftForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			new_shift = PostedShiftModel.objects.create(
				posted_by=request.user,
				start_time=data.get('start_time'),
				end_time=data.get('end_time'),
				date=data.get('date'),
				reason=data.get('reason')
				)
			return HttpResponseRedirect('/hourmanager/')

	else:
		form = PostShiftForm()


	context = {
		'hours' : OPEN_HOURS.values(),
		'shifts' : PostedShiftModel.objects.all(),
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