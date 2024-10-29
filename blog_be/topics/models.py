from django.db import models

# Create your models here.

class Story(models.Model):
    story_title = models.CharField(max_length=200)
    story_text = models.CharField(max_length=800)
