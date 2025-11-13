from django.http import HttpResponse

def index(request):
    return HttpResponse("Bookshelf app is working!")
