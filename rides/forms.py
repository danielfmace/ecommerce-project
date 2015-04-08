from rides.models import Student, Ride
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('has_car', 'seats', 'phone', 'avatar')
	def clean_avatar(self):
		avatar = self.cleaned_data['avatar']

		try:
			w, h = get_image_dimensions(avatar.path)

			#validate dimensions
			max_width = max_height = 100
			if w > max_width or h > max_height:
				raise forms.ValidationError(
					u'Please use an image that is '
					 '%s x %s pixels or smaller.' % (max_width, max_height))

			#validate content type
			main, sub = avatar.content_type.split('/')
			if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
				raise forms.ValidationError(u'Please use a JPEG, '
					'GIF or PNG image.')

			#validate file size
			if len(avatar) > (20 * 1024):
				raise forms.ValidationError(
					u'Avatar file size may not exceed 20k.')

		except AttributeError:
			"""
			Handles case when we are updating the user profile
			and do not supply a new avatar
			"""
			pass

		return avatar

class ScheduleForm(forms.Form):
	def __init__(self, ride, *args, **kwargs):
		super(ScheduleForm, self).__init__(*args, **kwargs)
		self.fields['rides'] = forms.ChoiceField(choices = [ (r.id, str(r)) for r in Ride.objects.filter(start = ride.start, dest = ride.start)])

class RideForm(forms.ModelForm):
	class Meta:
		model = Ride
		fields = ('start', 'dest', 'time', 'seats', 'driver')
		widgets = {'seats': forms.HiddenInput(), 'driver': forms.HiddenInput()}

