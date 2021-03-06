from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail
from django.urls import reverse
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=20)
    issue_a = models.CharField(max_length=20)
    issue_b = models.CharField(max_length=20)
    image_a = ProcessedImageField(
        processors=[Thumbnail(200,300)],
        format='JPEG', 
        options={'quality':90},
        upload_to='eithers/images', 
    )
    image_b = ProcessedImageField(
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90}, 
        upload_to='eithers/images', 
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question:detail', kwargs={'question_pk':self.pk})

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'<Question({self.question_id}): Answer({self.pk})-{self.comment}>'