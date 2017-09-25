from django.db import models

class Stove(models.Model):
	token = models.CharField(blank=False, max_length=45)