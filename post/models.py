from django.db import models
from django.utils import timezone


class University(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    email_domain = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class User(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    name = models.CharField(max_length=50)
    major = models.CharField(max_length=100)

    nationality = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    profile_image_url = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.name} - {self.interest.name}"


class Question(models.Model):
    question_text = models.TextField()
    category = models.CharField(max_length=50)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    answer_text = models.TextField()

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.name} - {self.question.id}"


class Match(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_matches"
    )

    matched_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_matches"
    )

    match_score = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        default="pending"
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.name} ↔ {self.matched_user.name}"


class Chat(models.Model):
    match = models.OneToOneField(
        Match,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Chat {self.id}"


class Message(models.Model):
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    message_type = models.CharField(
        max_length=20,
        default="text"
    )

    content = models.TextField()

    sent_at = models.DateTimeField(default=timezone.now)

    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.name}: {self.content[:20]}"