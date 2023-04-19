from django.db import models

# Create your models here.

class user1(models.Model):
    firstName = models.CharField(max_length=30, default='Yogesh')
    def __str__(self):
        return self.firstName


class action(models.Model):
    job = models.TextField(blank=True)
    jid = models.ForeignKey(user1, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.job