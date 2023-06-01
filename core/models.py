from django.db import models

# Nutzen wir für die anderen Models, hat keine eigene Table
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True # no table is created on db-level for this specific model