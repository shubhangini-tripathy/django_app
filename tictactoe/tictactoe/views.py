from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hello , World!")


def welcome_shubhi(request):
    return HttpResponse("Hello , shubhi")
