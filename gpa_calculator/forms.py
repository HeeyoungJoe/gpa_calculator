from .models import *
from django import forms
from archive.models import Archive
class CourseInputForm(forms.ModelForm):
    #model=models.ForeignKey(Course)
    class Meta:
        model=Course
        fields='__all__'

class Desired_standard(forms.ModelForm):
    class Meta:
        model=Archive
        fields=('desired_standard',)