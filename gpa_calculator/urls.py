from django.urls import path
from .views import *
urlpatterns = [
   # path('',main_page,name="main_page"),
    path('list/',CourseListView.as_view(),name="list"),
    path('',register,name="register"),

]
