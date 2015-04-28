from rides.models import Student, Ride
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django import forms
from datetime import datetime

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
		self.fields['rides'] = forms.ChoiceField(choices = [ (r.id, str(r)) for r in Ride.objects.filter(start = ride.start, dest = ride.dest, time__gte = datetime.now())])

class CancelDriveForm(forms.Form):
	def __init__(self, user, *args, **kwargs):
		super(CancelDriveForm, self).__init__(*args, **kwargs)
		self.fields['rides'] = forms.ChoiceField(choices = [ (r.id, str(r)) for r in Ride.objects.filter(driver = user, time__gte = datetime.now())])

class RiderReviewForm(forms.Form):
	def __init__(self, ride, *args, **kwargs):
		super(RiderReviewForm, self).__init__(*args, **kwargs)
		driver = ride.driver
		driver = Student.objects.get(user=driver)
		self.fields['subject'] = forms.ChoiceField(choices = [ (r.id, str(r)) for r in ride.riders.all() ])
		self.fields['comment'] = forms.CharField(max_length=2000)
		self.fields['rating'] = forms.ChoiceField(choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

class DriverReviewForm(forms.Form):
	def __init__(self, ride, *args, **kwargs):
		super(DriverReviewForm, self).__init__(*args, **kwargs)
		driver = ride.driver
		driver = Student.objects.get(user=driver)
		self.fields['subject'] = forms.ChoiceField(choices = [ (driver.id, str(driver))])
		self.fields['comment'] = forms.CharField(max_length=2000)
		self.fields['rating'] = forms.ChoiceField(choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

class RideForm(forms.ModelForm):
	class Meta:
		model = Ride
		fields = ('start', 'dest', 'time', 'seats', 'driver')
		widgets = {'seats': forms.HiddenInput(), 'driver': forms.HiddenInput()}

