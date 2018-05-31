from django import forms
from django.utils import timezone

from .models import HourModel, HourHistoryModel

class HourModelAddForm(forms.ModelForm):
    date        = forms.DateField()
    start_time  = forms.TimeField()
    end_time    = forms.TimeField()
    reason      = forms.CharField(max_length=120, required=False)

    def clean(self):
        super(HourModelAddForm, self).clean()
        now = timezone.now()

        if self.cleaned_data.get('date') < now:
            raise forms.ValidationError("Cannot post this date.")

        if self.cleaned_data.get('end_time') <= self.cleaned_data.get('start_time'):
            raise forms.ValidationError("Cannot have end time before start time")

    class Meta:
        model = HourModel
        fields = [
            "date",
            "start_time",
            "end_time",
            "reason"
        ]