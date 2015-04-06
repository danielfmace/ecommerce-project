from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login

from django.shortcuts import render, render_to_response
from rides.forms import UserForm, StudentForm
from django.template import RequestContext

from rides.models import User

@login_required
def index(request):
	users = User.objects.all()
	context = {'users': users}
	return render(request, 'rides/index.html', context)



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