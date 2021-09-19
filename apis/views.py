from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def firstapi(request):
    # return HttpResponse('We are doing well.')
    return render(request, 'firstapi.html')
    