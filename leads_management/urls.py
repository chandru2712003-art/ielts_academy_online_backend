

from rest_framework import routers
from .views import submit_form
from django.urls import path    


ulrpatterns=[
    path('submitform/', submit_form.as_view(), name='submit_form'),
]