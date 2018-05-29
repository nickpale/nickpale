import datetime

from django.db import models
from django.utils import timezone


class JournalEntry(models.Model):
    heading_text = models.CharField(max_length=200)
    entry_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.heading_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
