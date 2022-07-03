from django.urls import path


from .views import *

urlpatterns = [
    path('', function_of_view_main_page)
]
