from django.urls import path


from .views import *

urlpatterns = [
    path('', function_of_view_main_page, name="index"),
    path('add/', spreadsheet_view),
    path('date/', date_entry, name="date_entry")
]
