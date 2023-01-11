from django.shortcuts import HttpResponse


# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello!👋 It's my project")


def now_date(request):
    if request.method == 'GET':
        return HttpResponse('10 Jan')


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye!')
