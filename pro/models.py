from django.db import models


class Blurb(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    active = models.BooleanField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Ensures that there is only one active Blurb at a time."""
        if self.active:
            Blurb.objects.filter(active=True).update(active=False)
        super(Blurb, self).save(*args, **kwargs)


class Description(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    order_rank = models.IntegerField()

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=64)
    file = models.FileField(upload_to='pro/media/resumes')
    pub_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Ensures that there is only one active Resume at a time."""
        if self.active:
            Resume.objects.filter(active=True).update(active=False)
        super(Resume, self).save(*args, **kwargs)
