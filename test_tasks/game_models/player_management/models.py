from django.db import models
from django.utils import timezone


class Player(models.Model):
    username = models.CharField(max_length=50, unique=True)
    daily_points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    first_login = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    login_streak = models.IntegerField(default=0)


def __str__(self):
    return self.username


class BoostType(models.TextChoices):
    SPEED = 'SP', 'Speed'
    POWER = 'PW', 'Power'
    SHIELD = 'SH', 'Shield'


class Boost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='boosts')
    boost_type = models.CharField(max_length=2, choices=BoostType.choices)
    quantity = models.PositiveIntegerField(default=1)
    acquired_at = models.DateTimeField(default=timezone.now)
    expiration_time = models.DateTimeField(null=True, blank=True)


class PlayerDailyActivity(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='daily_activities')
    date = models.DateField(default=timezone.now)
    points_earned = models.IntegerField(default=0)
    login_time = models.DateTimeField(default=timezone.now)