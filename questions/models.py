import uuid as uuid_lib

from django.conf import settings
from django.db import models
from core.models import TimeStampedModel

# Create your models here.
class Question(TimeStampedModel):
    uuid = models.UUIDField(default=uuid_lib.uuid4, editable=False)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="questions") # related_name ist für reversed queries, dh. wir können alle questions von einem user finden
    
    def __str__(self):
        return self.content

class Answer(TimeStampedModel):
    uuid = models.UUIDField(db_index=True, default=uuid_lib.uuid4, editable=False)
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="answers")
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")
    
    def __str__(self):
        return self.author.username