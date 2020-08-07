import django.forms as forms
from vmwellnessapp.models import *

# Create the form class.
class ActiviesForm(forms.ModelForm):
    name = forms.CharField(required=False, initial='Anonymous')
    status = forms.CharField()
    class Meta:
        model = Activies
        fields = ['name', 'status']
        labels = {
            "name": "Name (leave blank if anonymous)",
            "status": "status"
        }


class InitialWaterTrackerForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ['consumptionGoal']
        labels = {
            "consumptionGoal": "Consumption Goal for the Day"
        }

class UpdateWaterTrackerForm(forms.ModelForm):
    additional_amount = forms.CharField(label='How much water have you had? ')
    class Meta:
        model = Water
        fields = []

class CheckGoalForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['goal']
        labels = {'goal': 'Goal'}