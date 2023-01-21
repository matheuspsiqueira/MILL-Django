from django.urls import path
from .views import *

urlpatterns = [
    path('estoque', estoque, name='estoque'),
]