from django.db import models
from django.db.models.expressions import F

class Event(models.Model):

    event_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey("Games", on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)