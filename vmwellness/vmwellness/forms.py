import django.forms as forms
from vmwellness.models import *

# Create the form class.
class ActiviesForm(forms.ModelForm):
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
    additional_amount = forms.CharField(label='Additional Amount of Water Consumed')
    class Meta:
        model = Water
        fields = []

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['goal_one', 'goal_two', 'goal_three','goal_four', 'goal_five']
        labels = {
            "goal_one": "First goal",
            "goal_two": "Second Goal",
            "goal_three": "Third Goal",
            "goal_four": "Fourth Goal",
            "goal_five": "Fifth Goal"
        }
