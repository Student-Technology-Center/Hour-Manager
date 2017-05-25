'''Hour manager sub directory views stored here'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from hour_manager.models import HourModel

from .forms import HourAddForm

def index(request):
    '''Return the index page.'''

    #Some linters may say this line below is invalid, it IS valid
    hours = HourModel.objects.all()

    context = {
        "hours":hours,
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
        instance.save()
        print(instance.first_name)

    context = {
        "form": form
    }

    return render(
        request,
        "hourmodel_form.html",
        context
    )
