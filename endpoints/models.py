from django.db import models

# Create your core here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=50)
    code_challenge = models.TextField()
