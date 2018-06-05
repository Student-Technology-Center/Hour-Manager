'''Hour manager sub directory views stored here'''
from django.contrib.auth.decorators import login_required
from login.decorators import user_is_email_confirmed
from django.shortcuts import render

from shiftmanager.models import Shift, ShiftFile

@login_required
@user_is_email_confirmed
def index(request):
    '''
    Return the index page to the hour manager
    '''

    print(Shift.objects.filter(user=request.user)[0].hourmodel_set)

    return render(
        request,
        'hour_manager_index.html',
        None
    )