from django.contrib import admin
from .models import Symptom, Disease, DiagnosisReport, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'blood_type')
    search_fields = ('user__username', 'blood_type')

@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('symptoms',)

@admin.register(DiagnosisReport)
class DiagnosisReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'matched_disease', 'accuracy', 'created_at')