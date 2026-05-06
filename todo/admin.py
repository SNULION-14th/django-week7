from django.contrib import admin
from .models import User, Profile, TodoList, Calendar, Routine  


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(TodoList)
admin.site.register(Calendar)
admin.site.register(Routine)
