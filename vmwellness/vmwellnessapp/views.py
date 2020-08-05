
from django.shortcuts import render
from django.http import HttpResponse
from vmwellnessapp.models import *
from django.views.generic import TemplateView

# Create your views here.


# create dashboard class
class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


# create a beautiful, elegant water class
class WaterTracker(TemplateView):
    template_name = 'water_tracker.html'

    def get(self, request):
        return render(request, self.template_name)


# create activity stream class
class ActivityStream(TemplateView):
    template_name = 'wellness_stream.html'

    def get(self, request):
        return render(request, self.template_name)


# create goals class
class Goals(TemplateView):
    template_name = 'goals.html'    # this should change to the goals html

    def get(self, request):
        return render(request, self.template_name)


# create resources class
class Resources(TemplateView):
    template_name = 'resources.html'

    def get(self, request):
        return render(request, self.template_name)


# create about class
class About(TemplateView):
    template_name = 'about.html'

    # def get(self, request):
    #     return render(request, self.template_name)
    pass