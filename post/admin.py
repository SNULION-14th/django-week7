from django.contrib import admin

from .models import School, Scholarship, User, ScholarshipMajor, ScholarshipIncome, UserScholarship


admin.site.register(School)
admin.site.register(Scholarship)
admin.site.register(User)
admin.site.register(ScholarshipMajor)
admin.site.register(ScholarshipIncome)
admin.site.register(UserScholarship)