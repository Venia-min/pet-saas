from django.db import models


class PageVisit(models.Model):
    # db -> table
    # id -> primary key -> autofield
    path = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
