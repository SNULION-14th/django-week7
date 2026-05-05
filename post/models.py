from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    tags = models.ManyToManyField(
        'Tag',
        through='PostTag',
        related_name='posts',
        blank=True,
    )

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    college = models.CharField(max_length=100)
    major = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} profile'


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:30]


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['post', 'user'],
                name='unique_like_per_user_post',
            ),
        ]

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'


class Tag(models.Model):
    content = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.content


class PostTag(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_tags',
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='post_tags',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['post', 'tag'],
                name='unique_tag_per_post',
            ),
        ]

    def __str__(self):
        return f'{self.post.title} - {self.tag.content}'
