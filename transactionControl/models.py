from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    transacBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_transactions'
    )
    transacTo = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_transactions'
    )
    amountSent = models.IntegerField()
    rewardAmountToSender = models.IntegerField()
    datetime = models.DateField(default='2023-09-02')


class Pair(models.Model):
    sender = models.ManyToManyField(User, related_name='sent_pairs')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_pairs'
    )
    toSend = models.IntegerField()
    receiverUPI = models.BigIntegerField(null=True)


class Confirmed(models.Model):
    transaction = models.OneToOneField(
        Transaction, on_delete=models.CASCADE, related_name='confirmation'
    )
    confirmed = models.BooleanField()
