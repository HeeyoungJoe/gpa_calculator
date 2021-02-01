from .views import *
from django.urls import path
urlpatterns = [
   # path('',main_page,name="main_page"),
    path('result/', result_view, name="result")
]
