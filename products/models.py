from django.db import models


# Create your models here.
class Players(models.Model):
    name = models.TextField()
    nations = models.TextField()
    team = models.TextField()
    city = models.TextField()


def __str__(self):
    return self.Name + ": " + str(self.id)
