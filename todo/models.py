from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username if self.username else self.id

class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    major = models.CharField(max_length=255)
    # ERD의 id2(FK)를 User 테이블과 연결합니다.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')

    def __str__(self):
        return self.name if self.name else self.id

DAY_CHOICES = [
    ('MON', '월요일'),
    ('TUE', '화요일'),
    ('WED', '수요일'),
    ('THU', '목요일'),
    ('FRI', '금요일'),
    ('SAT', '토요일'),
    ('SUN', '일요일'),
]

class Routine(models.Model):
    title = models.CharField(max_length=255)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    time = models.TimeField()
    field = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routines')

class TodoList(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    priority = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolists')

class Calendar(models.Model):
    cal_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendars')

	# 이건 print하면 어떤 값을 return할 지 알려주는 것!
    def __str__(self):
        return self.title
