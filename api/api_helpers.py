from django.http import JsonResponse

def hour_get(request, pk):
    return JsonResponse({
        "get" : "get"
    })

def hour_post(request, pk):
    return JsonResponse({
        "post" : "post"
    })

def hour_put(request, pk):
    return JsonResponse({
        "put" : "put"
    })

def hour_delete(request, pk):
    return JsonResponse({
        "delete" : "delete"
    })