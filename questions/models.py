from django.db import models

class Answer(models.Model):
    answer = models.TextField()
    art = models.ImageField(upload_to='questions/media/answer-art',
                            null=True,
                            blank=True)

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.TextField()
    pub_date = models.DateTimeField('date published')
    answer = models.ForeignKey(Answer,
                               blank=True,
                               null=True,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.question
