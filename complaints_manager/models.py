from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Category(models.Model):
    title = models.TextField(blank=False, null=False, unique=True)


class Complaint(models.Model):
    identity = models.TextField(blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category)
    likes = models.IntegerField(null=False, default=0)
    create_date = models.DateTimeField(null=False, default=timezone.now)


class PersonSummary(models.Model):
    identity = models.TextField(blank=False, null=False, unique=True)
    complaints = ArrayField(models.BigIntegerField(), blank=True)
    complaints_count = models.IntegerField(null=False, default=0)
