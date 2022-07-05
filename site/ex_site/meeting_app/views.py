from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import date, timedelta, datetime, time

from .models import *


def function_of_view_main_page(request):
    date_list = [dt.date_entry for dt in DateEntry.objects.all()]
    for obj in DateEntry.objects.all():
        if obj.date_entry < date.today():
            obj.delete()

    for i in range(1, 7):
        print(date.today())
        fix_date = date.today() + timedelta(days=i)
        print(fix_date)
        if fix_date not in date_list:
            fix = datetime.now() + timedelta(days=i)
            de_1 = DateEntry(date_entry=datetime(fix.year, fix.month, fix.day), time_entry=time(19, 0, 0)).save()
            de_2 = DateEntry(date_entry=datetime(fix.year, fix.month, fix.day), time_entry=time(20, 0, 0)).save()
    print([dt.date_entry for dt in DateEntry.objects.all()])

    customers = Customer.objects.all() 
    if request.method == 'POST':
        print(request.POST)
    return render(request, "meeting_app/index.html", {'customers' : customers, 'title' : 'Main page', 'body' : 'Year, its a main page'})




def spreadsheet_view(request):
    customers = Customer.objects.all() 
    print([cus.mail for cus in Customer.objects.filter(name="Slava")])
    return render(request, "meeting_app/table.html", {'customers' : customers, 'title' : 'Main page', 'body' : 'Year, its a main page'})




def date_entry(request):
    class SubClass:
        def __init__(self, obj, name):
            self.obj = obj    
            self.name = name

    if request.method == 'POST':
        print(request.POST)

    dates = [SubClass(dt, "ratio-" + str(i + 1)) for i, dt in enumerate(DateEntry.objects.all())]

    return render(request, "meeting_app/date_entry.html", {'dates' : dates, 'surname' : request.POST.get('Surname'), 'name' : request.POST.get('Name'), 'mail' : request.POST.get('Mail'), 'phone' : request.POST.get('Phone')})

#def validate
    

def null_page(request):
    return HttpResponse("<h3>Nice to meet you again:)</h3>")
    
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h2>DAMN!!! PAGE NOT FOUND</h2>")


# Create your views here.
