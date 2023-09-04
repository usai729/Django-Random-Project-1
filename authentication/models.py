from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userInfo(models.Model):
    ofUser = models.OneToOneField(User, on_delete=models.CASCADE)
    UPI = models.BigIntegerField()
    userReferralID = models.TextField()


class referredBy(models.Model):
    referredByUser = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    referredToUser = models.TextField()
