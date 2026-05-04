from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    pre_existing_conditions = models.TextField(blank=True) # 기저 질환
    medications = models.TextField(blank=True) # 복용 약물
    blood_type = models.CharField(max_length=5, blank=True) # 혈액형

    def __str__(self):
        return f"{self.user.username}의 프로필"

class Symptom(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    symptoms = models.ManyToManyField(Symptom, related_name='diseases')

    def __str__(self):
        return self.name

class DiagnosisReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matched_disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True)
    user_input_text = models.TextField()
    accuracy = models.IntegerField(default=0) # AI 확신도 (0-100)
    mri_scan = models.ImageField(upload_to='diagnoses/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.matched_disease.name if self.matched_disease else 'Unknown'}"