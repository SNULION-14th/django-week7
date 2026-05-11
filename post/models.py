from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.nickname


class Exhibition(models.Model):
    exhibition_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='logs'
    )

    exhibition = models.ForeignKey(
        Exhibition,
        on_delete=models.CASCADE,
        related_name='logs'
    )

    content = models.TextField()

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.nickname} - {self.exhibition.title}"


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)

    log = models.ForeignKey(
        Log,
        on_delete=models.CASCADE,
        related_name='photos'
    )

    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"Photo {self.photo_id} of Log {self.log_id}"
