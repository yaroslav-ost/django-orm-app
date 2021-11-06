from django.conf import settings
from django.db import models


class Url(models.Model):
    url_short = models.CharField(max_length=5, primary_key=True)
    url = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    redirect_count = models.IntegerField(default=0)
