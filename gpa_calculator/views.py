from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Course
from .calculator import calculate
from .forms import CourseInputForm
from django.views.generic import ListView
# Create your views here.
'''
def main_page(request):
    return render(request,'main_page.html')
'''

class CalculatorListView(ListView):
    model=Course
    template_name = 'main_page.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CourseInputForm()
        return context
    def get_list(self):
        return Course.objects.all()
'''    def input_course(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method=='POST':
            if context['form'].is_valid():
                return HttpResponseRedirect('main_page.html')
        return render(self.request, 'main_page.html', {'form': context['form']})
'''

