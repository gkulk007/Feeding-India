from django.db import models


class Submitform(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    line = models.TextField(blank=True)

    def __str__(self):
        return self.name