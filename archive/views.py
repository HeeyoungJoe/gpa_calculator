from django.shortcuts import render
from .models import Archive
from gpa_calculator.forms import Desired_standard
from gpa_calculator.calculator import calculate
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.

def result_view(request):
    model=Archive
    Archive.total_avg, Archive.major_avg, Archive.minor_avg, is_working = calculate(4.5)
    flag="result_view:"
    if request.method=='POST':
        flag+="POST"
        archive_form=Desired_standard(request.POST)
        if archive_form.is_valid():
            new_archive=archive_form.save(commit=False)
            new_archive.save()
            archive_object = Archive.objects.latest('desiredStandard')
            Archive.total_avg, Archive.major_avg, Archive.minor_avg, is_working = calculate(
                archive_object.desiredStandard)
    else:
        flag+="else"
        archive_form=Desired_standard()
    return render(request,'result.html',{'form':archive_form,'totavg':Archive.total_avg,'majavg':Archive.major_avg,'minavg':Archive.minor_avg,'is_working':flag,'desiredStandard':Archive.desiredStandard})
#desired_standard}

def test_api(request):
    archive_object=Archive.objects.latest('desiredStandard')
    Archive.total_avg, Archive.major_avg, Archive.minor_avg, is_working = calculate(archive_object.desiredStandard)
    return JsonResponse({'totavg':Archive.total_avg,'majavg':Archive.major_avg,'minavg':Archive.minor_avg,'desiredStandard':Archive.desiredStandard},status=201)