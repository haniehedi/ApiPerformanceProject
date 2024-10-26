from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='properties')
    def __str__(self):
        return self.title

