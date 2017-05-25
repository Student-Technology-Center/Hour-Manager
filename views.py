'''Hour manager sub directory views stored here'''
from django.shortcuts import render
from .models import HourModel

def index(request):
    '''Return the index page.'''

    hours = "Hello!"

    return render(
        request,
        'index.html',
        context=None
    )
