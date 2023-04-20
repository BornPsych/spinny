from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    def save(self, *args, **kwargs):
        if not self.pk or self._password != self.password:
            self.set_password(self.password)

        super().save(*args, **kwargs)

class Box(models.Model):
    length = models.FloatField(default=1)
    breadth = models.FloatField(default=1)
    height = models.FloatField(default=1)
    area = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boxes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def getArea(self):
        Box_area = self.length * self.breadth
        return Box_area

    def getVolume(self):
        Box_volume =  self.length * self.breadth * self.height
        return Box_volume

    def save(self, *args, **kwargs):
        self.area = self.getArea()
        self.volume = self.getVolume()
        instance = super(Box, self).save(*args, **kwargs)