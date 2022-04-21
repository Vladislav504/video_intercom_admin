from django.db import models
from django.contrib.postgres.fields import ArrayField


class Face(models.Model):
    name = models.CharField(verbose_name="name", primary_key=True, max_length=128)
    encoding = ArrayField(models.FloatField(), size=128, default=list)
