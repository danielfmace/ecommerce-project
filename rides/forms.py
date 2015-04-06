from rides.models import Student
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'first_name', 'last_name')

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ('has_car', 'seats', 'phone')