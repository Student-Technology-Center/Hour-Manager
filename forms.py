from django import forms

from .models import HourModel

class HourAddForm(forms.ModelForm):
    class Meta:
        model = HourModel
        fields = [
            "date",
            "start_time",
            "end_time",
            "reason",
        ]