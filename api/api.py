'''Hour manager sub directory views stored here'''
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
from hour_manager.models import HourModel

class Hour(View):
    def put(self, request, pk):
        return JsonResponse({
            "put" : "put"
        })

    def get(self, request, pk):
        return JsonResponse({
            "GET" : "GET"
        })

    def post(self, request, pk):
        return JsonResponse({
            "post" : "post"
        })

    def delete(self, request, pk):
        return JsonResponse({
            "del" : "del"
        })