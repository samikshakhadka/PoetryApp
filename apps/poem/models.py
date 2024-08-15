from django.db import models
from django.conf import settings
from django.utils import timezone

from apps.user.models import CustomUser

class Poem(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    poems = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'poem')