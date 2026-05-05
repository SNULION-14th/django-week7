from django.contrib import admin

# Register your models here.
from .models import User, Crew, CrewMember, CrewGoal, WorkoutLog, Donation
admin.site.register(User)
admin.site.register(Crew)
admin.site.register(CrewMember)
admin.site.register(CrewGoal)
admin.site.register(WorkoutLog)
admin.site.register(Donation)