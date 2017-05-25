from django import forms

from .models import HourModel

class HourAddForm(forms.ModelForm):
    class Meta:
        model = HourModel
        fields = [
            "first_name",
            "last_name",
            "date",
            "start_time",
            "end_time",
            "reason",
        ]