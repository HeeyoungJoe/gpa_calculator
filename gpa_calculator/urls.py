from django.urls import path
from .views import *
urlpatterns = [
   # path('',main_page,name="main_page"),
    path('',CalculatorListView.as_view(),name="list")

]