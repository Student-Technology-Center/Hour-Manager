from django import forms
from .models import PostedShiftModel, OPEN_HOURS
from datetime import datetime, date, time

today = date.today().strftime("%B %d, %Y")

class PostShiftForm(forms.Form):
	date = forms.DateField(
		input_formats=['%B %d, %Y'], 
		widget=forms.TextInput(attrs={'id':'date-value','placeholder':today,'autocomplete':'off'}))
	start_time = forms.TimeField(
		label='Start Time', 
		input_formats=['%I:%M%p'])
	end_time = forms.TimeField(
		label='End Time', 
		input_formats=['%I:%M%p'])
	reason = forms.CharField(
		max_length=300,
		widget=forms.Textarea(attrs={'placeholder':'Why give up a shift?','rows':'3'}))

	# Adding to default form validation to ensure that the start/end time is valid
	def clean(self):
		cleaned_data = super().clean()
		s_t 	= cleaned_data.get('start_time')
		e_t 	= cleaned_data.get('end_time')
		date 	= cleaned_data.get('date')

		if s_t and e_t and s_t >= e_t:
			raise forms.ValidationError(
				('End time must be after start time'),
				code='invalid_times'
				)

		if date and date < date.today():
			raise forms.ValidationError(
				('Can\'t post shifts from the past'),
				code='past_date'
				)
