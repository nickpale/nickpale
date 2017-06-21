from django.db import models

class Outfit(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=20)
    description = models.TextField(blank=True, default='')
    art = models.ImageField(upload_to='music/media/outfit-art', null=True, blank=True)
    bandcamp = models.URLField(blank=True, default='')

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=80)
    slug = models.CharField(max_length=20)
    description = models.TextField(blank=True, default='')
    art = models.ImageField(upload_to='music/media/album-art', null=True, blank=True)
    credits = models.TextField(blank=True, default='')
    pub_date = models.DateTimeField('date published')
    bandcamp = models.URLField(blank=True, default='')
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pub_date']


def album_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/music/media/audio/<album>/<filename>
    return 'music/media/{0}/{1}'.format(instance.album.name, filename)

class Track(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=20)
    audio = models.FileField(upload_to=album_directory_path)
    pub_date = models.DateTimeField('date published')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pub_date']
