from django.contrib.auth.models import AbstractUser # Wir müssen nicht unbedingt eine neue Spalte in den models erzeugen, wenn wir das hier verwenden

# Müssen wir nichts eintragen bei AbstractUser
class CustomUser(AbstractUser):
    pass
