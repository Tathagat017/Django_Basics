
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><h1>Hey there buddy! Death is eternal.You're at the polls index.</h1><p>Django View</p></html>")
    

# Create your views here.
