from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.views import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vmwellnessapp.models import *
from django.views.generic import TemplateView
#from vmwellness.forms import SignUpForm

# Create your views here.
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "registration/login.html",
                  context={"form":form})

def signup(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/dashboard')
    else:
        f = UserCreationForm()
    return render(request = request,
                  template_name = "registration/signup.html",
                  context={"form":f})

def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request=request,
                      template_name="registration/logout.html")
    else:
        return redirect('/dashboard')

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