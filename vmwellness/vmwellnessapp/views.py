from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.views import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from vmwellnessapp.models import Water, Activies, Checklist
from django.views.generic import TemplateView

from vmwellness.forms import *
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
            new_user = authenticate(username=f.cleaned_data['username'],
                                    password=f.cleaned_data['password1'],
                                    )
            login(request, new_user)
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


# returns true if a user is logged in given a request, otherwise false
def is_logged_in(request):
    return str(request.user) != 'AnonymousUser'


# create dashboard class
class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request):
        # added to check login status on dashboard
        args = {'username': ''}
        if is_logged_in(request):
            # user is logged in update args to reflect that
            args['username'] = ' ' + str(request.user)

        return render(request, self.template_name, args)


# create a beautiful, elegant water class
class WaterTracker(TemplateView):
    template_name = 'water_tracker.html'

    # get information on the amount of water consumed and the water intake  goal
    def get(self, request):
        # in the future be able to make request with no objects
        # check to make user is logged on:
        try:
            obj = Water.objects.get(userId=request.user)
            form = UpdateWaterTrackerForm()
            water_consumed = obj.currAmountConsumed
            consumption_goal = obj.consumptionGoal
            percent_complete = round(water_consumed/consumption_goal * 100, 2)
            args = {
                    'form': form,
                    'water_consumed': water_consumed,
                    'water_goal': consumption_goal,
                    'percent_complete': percent_complete,
                    'is_put': True
                }
        except:
            form = InitialWaterTrackerForm()
            args = {'form': form, 'is_put': False}

        return render(request, self.template_name, args)


    # post function that merges put and post requests
    def post(self, request):
        form = None
        try:
            # try a put by checking if obj throws an error, otherwise catch with post req
            obj = Water.objects.get(userId=request.user)
            
            # obj exists so proceed with put request
            form = UpdateWaterTrackerForm(request.POST)
            if form.is_valid:
                # get the user entered data and calculate new amount
                req_data = request.POST.copy()
                total_consumed = obj.currAmountConsumed + int(req_data.get('additional_amount'))
                # add user data to the Water db
                _, created = Water.objects.update_or_create(
                    userId = request.user,
                    defaults = {'currAmountConsumed': total_consumed}
                )
                # ensure new object was not created
                if created:
                    Exception('Error: db object created instead of modified')
                
                # redirect back to water page if successful
                return redirect('/water')
        except:
            # except means that there are no current Water db objs so create one for user
            form = InitialWaterTrackerForm(request.POST)
            if form.is_valid():
                # create and populate new water_obj fields
                water_obj = form.save(commit=False)
                water_obj.userId = request.user
                water_obj.currAmountConsumed = 0
                water_obj.save()

                # post was successful so redirect back to water
                return redirect('/water')
            
        # if both put and post don't return, render the form again
        return render(request, self.template_name, {'form':form})



# create activity stream class
class ActivityStream(TemplateView):
    template_name = 'wellness_stream.html'

    def get(self, request):
        form = ActiviesForm()
        activies = Activies.objects.order_by('-post_time') #query set which contains stuff from the table
        args = {'activies': activies, 'form': form, 'do_post':True}

        return render(request, self.template_name, args)

    def post(self, request):
        form = ActiviesForm(request.POST)
        if form.is_valid():
            activity_input = form.save(commit=False) #initializing a db obj based off of what user put
            activity_input.userId = request.user #attaching user to activity_input, populating that field
            activity_input.save()
            return redirect('/activitystream')

        args = {'form':form}
        return render(request, self.template_name, args)

# create goals class
def goals(request):
    goals = Checklist.objects.filter(userId=request.user)
    return render(request, 'goals.html', {'goals':goals})

def addGoalView(request):
    x = request.POST['goal']
    new_goal = Checklist(goal = x, userId=request.user)
    new_goal.save()
    return HttpResponseRedirect('/goals') 

def deleteGoalView(request, goal):
    y = Checklist.objects.get(id= goal)
    y.delete()
    return HttpResponseRedirect('/goals')


# create resources class
class Resources(TemplateView):
    template_name = 'resources.html'

    def get(self, request):
        return render(request, self.template_name)


# create about class
class About(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name)