from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Box(models.Model):
    length = models.FloatField(default=1)
    breadth = models.FloatField()
    height = models.FloatField()
    area = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def area(self):
        Box_area = self.length * self.breadth
        self.area = Box_area
        return Box_area

    def volume(self):
        Box_volume =  self.length * self.breadth * self.height
        self.volume = Box_volume
        return Box_volume

    def save(self):
        instance = super(Box, self).save()