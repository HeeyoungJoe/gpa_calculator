
from django.shortcuts import render,redirect
from .models import Course
from .forms import CourseInputForm
from django.views.generic import ListView
# Create your views here.
'''
def main_page(request):
    return render(request,'main_page.html')
'''
def register(request):
    if request.method=='POST':
        course_form=CourseInputForm(request.POST)
        if course_form.is_valid():
            new_course=course_form.save(commit=False)
            new_course.save()

    else:
        course_form=CourseInputForm()

    return render(request, 'main_page.html', {'form': course_form})
class CourseListView(ListView):
    model=Course
    template_name = 'list.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CourseInputForm()
        return context



