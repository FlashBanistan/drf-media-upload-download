from django.db import models
from django.contrib.auth.models import User

class Upload(models.Model):
    belongs_to = models.ForeignKey(User)
    video = models.FileField(upload_to='videos/')