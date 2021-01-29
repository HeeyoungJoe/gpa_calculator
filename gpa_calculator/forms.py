from .models import *
from django import forms
class CourseInputForm(forms.ModelForm):
    #model=models.ForeignKey(Course)
    class Meta:
        model=Course;
        fields='__all__'