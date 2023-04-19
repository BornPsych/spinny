from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Box(models.Model):
    length = models.FloatField(default=1)
    breadth = models.FloatField(default=1)
    height = models.FloatField(default=1)
    area = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def getArea(self):
        Box_area = self.length * self.breadth
        return Box_area

    def getVolume(self):
        Box_volume =  self.length * self.breadth * self.height
        return Box_volume

    def save(self, *args, **kwargs):
        self.volume = self.getVolume()
        self.area = self.getArea()
        super(Box, self).save(*args, **kwargs)