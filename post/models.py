from django.db import models
from django.contrib.auth.models import AbstractUser

# Django의 기본 유저 모델을 확장하여 trust_score를 추가합니다.
# (settings.py에 AUTH_USER_MODEL = '앱이름.User' 설정이 필요합니다.)
class User(AbstractUser):
    # username, email, password는 AbstractUser에 기본적으로 포함되어 있습니다.
    trust_score = models.FloatField(default=36.5, help_text="매너 온도 (기본 36.5도)")

    def __str__(self):
        return self.username
    
#class User(models.Model):
#    user_id = models.AutoField(primary_key=True)
#    username = models.CharField(max_length=50)
#    email = models.EmailField(unique=True)
#    password = models.CharField(max_length=128)
#    trust_score = models.FloatField(default=36.5)


class Profile(models.Model):
    # primary_key=True를 설정하여 기본 id 대신 profile_id를 사용합니다.
    profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    university = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}의 프로필"


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20, unique=True, verbose_name="ISBN")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    edition = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.edition})"


class Post(models.Model):
    # 상태값을 관리하기 위한 Choices
    STATUS_CHOICES = [
        ('AVAILABLE', '대여 가능'),
        ('RESERVED', '예약 중'),
        ('RENTED', '대여 중'),
    ]

    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    condition = models.TextField()
    deposit = models.PositiveIntegerField(help_text="보증금")
    rental_fee = models.PositiveIntegerField(help_text="대여료")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_content = models.TextField()
    is_secret = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}의 댓글"


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('ONGOING', '진행 중'),
        ('COMPLETED', '반납 완료'),
        ('OVERDUE', '연체 됨'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='transactions')
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_transactions')
    start_date = models.DateField()
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True) # 아직 반납 안 했을 수 있으므로 null 허용
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ONGOING')

    def __str__(self):
        return f"거래: {self.post.title} -> {self.borrower.username}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, related_name='review')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(help_text="1~5점 사이의 별점")
    review_content = models.TextField()

    def __str__(self):
        return f"{self.reviewer.username}의 리뷰"