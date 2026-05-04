from django.contrib import admin
from .models import User, Task, Scheduled_task, Task_history, Fixed_schedule

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Scheduled_task)
admin.site.register(Task_history)
admin.site.register(Fixed_schedule)