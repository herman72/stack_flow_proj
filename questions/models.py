from django.db import models
from django.urls import reverse
from users.models import User


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvoters = models.ManyToManyField(User, related_name='upvoted_questions')
    downvoters = models.ManyToManyField(User, related_name='downvoted_questions')
    tags = models.ManyToManyField('Tag', related_name='questions')

    def votes(self):
        return self.upvoters.count() - self.downvoters.count()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)



class Answer(models.Model):
    pass
