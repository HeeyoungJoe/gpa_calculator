from django.shortcuts import render
from .models import Archive
from gpa_calculator.forms import Desired_standard
# Create your views here.

def result_view(request):
    model=Archive
    if request.method=='POST':
        archive_form=Desired_standard(request.POST)
        if archive_form.is_valid():
            new_archive=archive_form.save(commit=False)
            new_archive.save()
    else: archive_form=Desired_standard()
    return render(request,'result.html',{'total average':Archive.total_avg,'major average':Archive.major_avg,'minor average':Archive.minor_avg})

