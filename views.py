'''Hour manager sub directory views stored here'''
from datetime import datetime
from random import randint
from datetime import date
import logging
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from hour_manager.models import HourModel, hour_history
from login.models import UserOptions, UserOptionsForm
from .forms import HourAddForm

from utils.alerts.alerter import email

#Creates a global logger object.
logger = logging.getLogger(__name__)

@login_required
def index(request):
    '''Return the index page.'''

    easter_egg = randint(0, 100)

    date_obj = datetime.now()

    current_time = date_obj.time()
    current_date = date_obj.date()

    #Some linters may say this line below is invalid, it IS valid
    hours = HourModel.objects.all()

    #Remove all previous dates, everytime someone loads the page
    for i in hours:
        if (i.date < current_date and i.start_time < current_time):
            i.delete()
        if i.pk is None:
            i.delete()

    if request.method == "POST":
        return "Hey."

    context = {
        "hours":hours,
        "any_hours":len(hours) == 0,
        "egg": easter_egg == 77
    }

    return render(
        request,
        'index.html',
        context
    )

@login_required
def AddHour(request, pk):
    '''Page to add hours to the hour manager'''
    form = HourAddForm(request.POST or None)
    context = {
            "form": form
        }

    if pk is None:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user.username
            instance.first_name = request.user.first_name
            instance.last_name = request.user.last_name
            instance.save()
            
            #Alert all members that opted in for emails.
            for user in User.objects.all():
                options = UserOptions.objects.get_or_create(user=user)

                if options[1]:
                    logger.warn("Had to create UserOptions for {}.".format(user.username))

                print("{} - Texting: {} Email: {}.".format(user.username, options[0].texting, options[0].email))

                if options[0].email:
                    message = "{} {} has just put hours up on the hour manager.\nFrom {} to {} on {}\nBecause: {}".format(instance.first_name, instance.last_name, 
                                                                                                                        instance.start_time, instance.end_time,
                                                                                                                        instance.date, instance.reason)
                    #email(user.email, "[STC] News hours on {}!".format(instance.date), message)
                    logger.info("Emailed user {} that a new hour is up!".format(user.username))
                    print("Emailed user {} that a new hour is up!".format(user.username))
                    print("{}".format(message))

            return HttpResponseRedirect("/hourmanager")

    if pk is not None:
        context['add'] = True

        if request.method == 'POST':
            if request.POST.get('delete') == 'Delete':
                old = HourModel.objects.get(pk=pk)
                old.delete()
                return HttpResponseRedirect("/hourmanager")

        if form.is_valid():
            old = HourModel.objects.get(pk=pk)

            if request.user.username != old.username:
                return HttpResponseRedirect("/hourmanager")

            old.date = form.cleaned_data.get('date')
            old.start_time = form.cleaned_data.get('start_time')
            old.end_time = form.cleaned_data.get('end_time')
            old.reason = form.cleaned_data.get('reason')
            old.save()
            return HttpResponseRedirect("/hourmanager")

    return render(
        request,
        "hourmodel_form.html",
        context
    )

@login_required
def claim_page(request, pk):
    '''Uses the hidden primary key of a table to retain which person is being covered'''

    shift = HourModel.objects.get(pk=pk)

    hour_history.objects.create(cover_username = request.user.username,
                                coveree_first = shift.first_name,
                                coveree_last = shift.last_name,
                                date = shift.date,
                                start_time = shift.start_time,
                                end_time = shift.end_time)
    shift.delete()
    
    return HttpResponseRedirect("/hourmanager")

@login_required
def comments(request):
    context = { }

    #Ensure the get goes through and is what we need.
    if request.method == 'GET':
        start = request.GET.get('start')
        end = request.GET.get('end')
        if (start and end):

            #Format dates for easy comparison
            start = start.split('-')
            end = end.split('-')

            try:
                start_date = date(int(start[0]), int(start[1]), int(start[2]))
                end_date = date(int(end[0]), int(end[1]), int(end[2]))
                shifts = hour_history.objects.all()
            except:
                return render(
                    request,
                    "comments.html",
                    { "date_err": True }
                )

            context["comments"] = []
            context["show_table"] = True

            for i in shifts:
                if (i.date >= start_date and i.date <= end_date):
                    context["comments"].append(i)
                    
    return render(
        request,
        "comments.html",
        context
    )

def history(request):

    context = {
        "history": hour_history.objects.all()
    }

    return render(
        request,
        "history.html",
        context
    )