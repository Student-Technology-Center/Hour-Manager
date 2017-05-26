'''Hour manager sub directory views stored here'''
from datetime import datetime
from random import randint

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from hour_manager.models import HourModel

from .forms import HourAddForm

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

    if len(hours) == 0:
        return render(
            request,
            'nohours.html',
            context = None
        )


    context = {
        "hours":hours,
    }

    return render(
        request,
        'index.html',
        context
    )

def AddHour(request):
    '''Page to add hours to the hour manager'''
    form = HourAddForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance.first_name)
        return HttpResponseRedirect("/hourmanager")

    context = {
        "form": form
    }

    return render(
        request,
        "hourmodel_form.html",
        context
    )

def claim_page(request, pk):
    '''Uses the hidden primary key of a table to retain which person is being covered'''
    
    shift = HourModel.objects.get(pk=pk)

    context = {
        "shift":shift
    }

    return render(
        request,
        "claimpage.html",
        context
    )
