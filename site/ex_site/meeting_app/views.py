from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *


def function_of_view_main_page(request):
    customers = Customer.objects.all() 
    return render(request, "meeting_app/index.html", {'customers' : customers, 'title' : 'Main page', 'body' : 'Year, its a main page'})

def null_page(request):
    return HttpResponse("<h3>Nice to meet you again:)</h3>")
    
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h2>DAMN!!! PAGE NOT FOUND</h2>")


# Create your views here.
