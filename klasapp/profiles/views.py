from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the page for user profiles.")