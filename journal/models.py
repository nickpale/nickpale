from django.db import models

class JournalEntry(models.Model):
    heading_text = models.CharField(max_length=200)
    entry_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.entry_text
