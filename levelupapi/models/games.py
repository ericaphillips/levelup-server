from django.db import models
from django.db.models.fields import CharField

class Games(models.Model):
    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=75)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    skill_level = models.IntegerField()