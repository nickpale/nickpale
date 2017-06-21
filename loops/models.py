from django.db import models

class Loop(models.Model):
    loop_file = models.FileField(upload_to='loops/media/%Y/%m')
    title = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
