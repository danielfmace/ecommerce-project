from django.contrib import admin
from rides.models import Student, Ride, Location, Start, Dest

admin.site.register(Student)
admin.site.register(Ride)
admin.site.register(Location)
admin.site.register(Start)
admin.site.register(Dest)

# Register your models here.
