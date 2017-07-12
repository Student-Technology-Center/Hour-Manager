from django import forms

from .models import HourModel

from datetime import datetime

class HourAddForm(forms.ModelForm):
    class Meta:
        model = HourModel
        fields = [
            "date",
            "start_time",
            "end_time",
            "reason",
        ]

    def clean(self):
        super(HourAddForm, self).clean()
        date = self.cleaned_data.get('date', False)
        start_time = self.cleaned_data.get('start_time', False)
        end_time = self.cleaned_data.get('end_time', False)

        date_obj = datetime.now()
        current_time = date_obj.time()
        current_date = date_obj.date()

        if date < current_date:
            raise forms.ValidationError(
                    "Please enter a day after today's date"
                )

        if end_time < start_time:
            raise forms.ValidationError(
                    "Please make sure your end time is after your start time"
                )