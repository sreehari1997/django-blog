from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    FAKE = 'F'
    TRUTH = 'T'

    FAKE_CHOICES = [
        (FAKE, 'Fake'),
        (TRUTH, 'Truth')
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    fake = models.CharField(max_length=1, choices=FAKE_CHOICES, default=FAKE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    @property
    def get_like_count(self):
        return self.like_set.all().count()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title
