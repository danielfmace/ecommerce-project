from django.http import HttpResponse

from django.shortcuts import render

from rides.models import User

def index(request):
	users = User.objects.all()
	context = {'users': users}
	return render(request, 'rides/index.html', context)