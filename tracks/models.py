from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Track(models.Model):
    # id auto created
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    track = models.ForeignKey('tracks.Track', related_name='likes', on_delete=models.CASCADE)
