from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


class suggestions(models.Model):
    comments = GenericRelation(Comment)

# Create your models here.
