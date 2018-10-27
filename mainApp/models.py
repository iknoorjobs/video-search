from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudyGroup(models.Model):
	venue = models.CharField(blank=False, max_length=1000)
	time = models.CharField(blank=False, max_length=1000)
	topic = models.CharField(blank=False, max_length=1000)
	date =  models.CharField(blank=False, max_length=1000)
	by = models.OneToOneField(User, on_delete=models.CASCADE, default=1)

	