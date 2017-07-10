'''Hour manager sub directory views stored here'''
from datetime import datetime
from random import randint

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from hour_manager.models import HourModel, hour_history

from .forms import HourAddForm

@login_required
def index(request):
    '''Return the index page.'''
    
    date_obj = datetime.now()

    current_time = date_obj.time()
    current_date = date_obj.date()

    #Remove all previous dates, everytime someone loads the page
    for i in HourModel.objects.all():
        if (i.date < current_date and i.start_time < current_time):
            i.delete()
        
    #Some linters may say this line below is invalid, it IS valid
    hours = HourModel.objects.all()

    context = {
        "hours":hours,
        "any_hours":len(hours) == 0
    }

    return render(
        request,
        'index.html',
        context
    )

@login_required
def AddHour(request):
    '''Page to add hours to the hour manager'''
    form = HourAddForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.first_name = request.user.first_name
        instance.last_name = request.user.last_name
        instance.save()
        return HttpResponseRedirect("/hourmanager")

    context = {
        "form": form
    }

    return render(
        request,
        "hourmodel_form.html",
        context
    )

@login_required
def claim_page(request, pk):
    '''Uses the hidden primary key of a table to retain which person is being covered'''

    shift = HourModel.objects.get(pk=pk)

    hour_history.objects.create(cover_username = request.user,
                                coveree_first = shift.first_name,
                                coveree_last = shift.last_name,
                                date = shift.date,
                                start_time = shift.start_time,
                                end_time = shift.end_time)

    shift.delete()
    
    return HttpResponseRedirect("/hourmanager")

@login_required
def comments(request):
    
    user = request.user
    shifts = []

    for i in hour_history.objects.all():
        if i.cover_username == user:
            shifts.append

    context = {
        "shifts":shifts
    }

    return render(
        request,
        "comments.html",
        context
    )

def history(request):
    
    shifthistory = hour_history.objects.all()

    context = {
        "history":shifthistory
    }

    return render(
        request,
        "history.html",
        context
    )