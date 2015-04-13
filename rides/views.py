from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login

from django.shortcuts import render, render_to_response
from rides.forms import UserForm, StudentForm, RideForm, ScheduleForm
from django.template import RequestContext

from django.contrib.auth.models import User
from rides.models import Student, Ride

@login_required
def index(request):
	context = RequestContext(request)
	current_user = request.user
	scheduled_ride = ""
	scheduled = ""
	current_student = Student.objects.get(user=current_user)
	if (request.method == 'POST'):
		# Attempt to grab information from the raw form information.
		ride_form = RideForm(initial={'seats': current_student.seats, 'driver': current_user}, data=request.POST)

		# If the form is valid...
		if ride_form.is_valid():
			ride = ride_form.save()
			str_start = str(ride_form.cleaned_data['start'])
			str_dest = str(ride_form.cleaned_data['dest'])
			str_time = str(ride_form.cleaned_data['time'])
			scheduled = "Thanks for scheduling your ride!"
			scheduled_ride = "Start: " + str_start + ", Dest: " + str_dest + ", Time: " + str_time
		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print(ride_form.errors)
	# Not a HTTP POST, so we render our form using a ModelForm instance
	# This will be blank, ready for user input.
	else:
		ride_form = RideForm(initial={'seats': current_student.seats, 'driver': current_user})

	# Render the template depending on the context.
	return render_to_response(
			'rides/index.html',
			{'ride_form': ride_form, 'scheduled_ride': scheduled_ride, 'scheduled': scheduled},
			context)

def cancel(request):
	context = RequestContext(request)
	current_user = request.user
	current_student = Student.objects.get(user=current_user)
	ride_id = request.POST['submitButton']
	ride = Ride.objects.get(id=ride_id)
	ride.riders.remove(current_student)

	return render_to_response(
		'rides/cancel.html',
		{'ride': ride},
		context)

@login_required
def schedule(request):
	context = RequestContext(request)
	# Get current user and student information
	current_user = request.user
	current_student = Student.objects.get(user=current_user)
	# Get ride_id from request.POST
	ride_id = request.POST['rides']
	ride = Ride.objects.get(id=ride_id)
	ride.riders.add(current_student)
	return render_to_response(
			'rides/schedule.html',
			{'ride': ride},
			context)

@login_required
def profile(request):
	context = RequestContext(request)
	# Get current user and student
	current_user = request.user
	current_student = Student.objects.get(user=current_user)

	return render_to_response(
		'rides/profile.html',
		{'current_user': current_user, 'current_student': current_student},
		context)

@login_required
def search(request):
	context = RequestContext(request)
	# Get current user and student information
	current_user = request.user
	current_student = Student.objects.get(user=current_user)
	
	# Generate ride_form from POST data
	ride_form = RideForm(initial={'seats': current_student.seats, 'driver': current_user}, data=request.POST)
	if ride_form.is_valid():
		# Construct a ride object from ride_form
		ride = ride_form.save(commit=False)
		start = ride.start
		dest = ride.dest
		time = ride.time
		identity = ride.id
		ride.driver = current_user
	else:
		print(ride_form.errors)
	rides = Ride.objects.filter(start=start, dest=dest)
	schedule_form = ScheduleForm(ride)
	return render_to_response(
			'rides/search.html',
			{'schedule_form': schedule_form, 'ride_form': ride_form, 'start': start, 'dest': dest, 'time': time, 'rides': rides, 'identity': identity},
			context)



def register(request):
	# Like before, get the request's context.
	context = RequestContext(request)

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)
		student_form = StudentForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and student_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			student = student_form.save(commit=False)
			student.user = user
			if 'avatar' in request.FILES:
				student.avatar = request.FILES['avatar']
			# Now we save the UserProfile model instance.
			student.save()

			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print(user_form.errors, student_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		student_form = StudentForm()

	# Render the template depending on the context.
	return render_to_response(
			'rides/register.html',
			{'user_form': user_form, 'student_form': student_form, 'registered': registered},
			context)

