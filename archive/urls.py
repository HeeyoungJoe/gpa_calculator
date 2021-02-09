from .views import *
from django.urls import path
urlpatterns = [
    path('result/', result_view, name="result")
]
