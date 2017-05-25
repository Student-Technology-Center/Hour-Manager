'''Hour manager sub directory views stored here'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import HourModel
from .forms import HourAddForm

def index(request):
    '''Return the index page.'''

    hours = "Hello!"

    return render(
        request,
        'index.html',
        context=None
    )

@login_required
def AddHour(request):
    form = HourAddForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print (instance.first_name)

    context = {
        "form": form
    }

    return render(
        request,
        "hourmodel_form.html",
        context
    )
