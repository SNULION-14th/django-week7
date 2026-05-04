# Model 관련 fields, methods를 모아놓은 놈입니다
from django.db import models

# 현재 시간 알기 위해
from django.utils import timezone

# # models.Model을 상속하여 Post라는 class를 선언해줍니다
# class Post(models.Model):
#     # title은 최대 256자의 character!
#     title = models.CharField(max_length=256)

#     # content는 글자 제한 없는 텍스트
#     content = models.CharField()

#     # created_at의 경우는 현재 시간 자동으로 입력되게!
#     created_at = models.DateTimeField(default=timezone.now)

#     # 이건 print하면 어떤 값을 return할 지 알려주는 것!
#     def __str__(self):
#         return self.title


class Major(models.Model):
    MName = models.CharField(max_length=100, primary_key=True)
    College = models.CharField(max_length=100)

    def __str__(self):
        return self.major_name


class User(models.Model):
    # ID : integer
    ID = models.IntegerField(primary_key=True)
    # Name:(
    name = models.CharField(max_length=50)
    interest = models.ForeignKey(
        Major, on_delete=models.SET_NULL, null=True, related_name="interested_users"
    )
    major_name = models.ForeignKey(
        Major, on_delete=models.SET_NULL, null=True, related_name="majored_users"
    )
    # level
    Level = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    Code = models.CharField(max_length=100)
    LName = models.CharField(max_length=100)
    CourseLevel = models.IntegerField(default=0)
    Category = models.CharField(max_length=50, default="교양")

    major_name = models.ForeignKey(
        Major, on_delete=models.CASCADE, related_name="lectures"
    )

    def __str__(self):
        return self.name


class PreRequisiteRelation(models.Model):
    lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name="required_by"
    )
    pre_lecture = models.ForeignKey(
        Lecture, on_delete=models.CASCADE, related_name="prerequisite_for"
    )


class CourseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    major_name = models.ForeignKey(Major, on_delete=models.CASCADE)
