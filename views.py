from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

@login_required
def index(request):
    context = { }
    return render(
        request,
        'hour_manager_index.html',
        context
    )