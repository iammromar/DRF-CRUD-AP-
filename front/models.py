from django.db import models

# Create your models here.


class edu(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    img = models.ImageField(upload_to='img/', null=True, blank=True)
    desc = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.title

