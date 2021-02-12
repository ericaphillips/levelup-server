from django.db import models
from django.db.models.expressions import F

class Event(models.Model):

    date = models.DateField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False)