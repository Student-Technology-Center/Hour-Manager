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
                'Cannot post an hour before the current date.'
                )

        if end_time < start_time:
            raise forms.ValidationError(
                "Please make sure your end time is after your start time"
            )

        if end_time < current_time:
            raise forms.ValidationError(
                "Your end time cannot be before the current time."
            )