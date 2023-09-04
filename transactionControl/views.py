from .models import Transaction, Pair
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Transaction, Pair, Confirmed
from django.shortcuts import render, HttpResponse
from .models import *
from django.http import JsonResponse
from django.core import serializers
from authentication.models import userInfo

import random
from datetime import datetime, timedelta
import time
import random
import json
# Create your views here.


def adminView(request):
    pairing(request)

    transactions_getAll = Transaction.objects.all()
    allTransactions = []
    allPairs = []

    for transaction in transactions_getAll:
        transaction_data = {
            'id': transaction.id,
            'by': transaction.transacBy,
            'to': transaction.transacTo,
            'amountSent': transaction.amountSent,
            'reward': transaction.rewardAmountToSender,
            'date': transaction.datetime
        }
        allTransactions.append(transaction_data)

    pairs = Pair.objects.all()

    for pair in pairs:
        pairData = {
            'pairID': pair.id,
            'sender': [sender.username for sender in pair.sender.all()],
            'receiver': pair.receiver.username,
            'amt': pair.toSend,
            'UPIr': pair.receiverUPI
        }
        allPairs.append(pairData)

    print(len(allPairs))

    transactions_getConfirmed = Transaction.objects.filter(
        confirmation__confirmed=True)

    try:
        confirmedTransactions = []
        totalAvailableStock = 0

        for transaction in transactions_getConfirmed:
            transaction_data = {
                'id': transaction.id,
                'by': transaction.transacBy,
                'to': transaction.transacTo,
                'amountSent': transaction.amountSent,
                'reward': transaction.rewardAmountToSender,
                'error': False
            }
            confirmedTransactions.append(transaction_data)

            totalAvailableStock += transaction.rewardAmountToSender
    except Exception as e:
        confirmedTransactions = {
            'error': str(e)
        }
        totalAvailableStock = 0

    return render(request, 'admin-view.html', {'transactions_all': allTransactions, 'transactions_confirmed': confirmedTransactions, 'pairs': allPairs, 'available_stock': totalAvailableStock})


def pairing(request):
    if len(Pair.objects.all()) > 0:
        Pair.objects.all().delete()

    max_send = 2000
    min_send = 1

    today = datetime.now().date()

    transactions = Transaction.objects.filter(confirmation__confirmed=True)

    pairings = []

    try:
        for transaction in transactions:
            transacBy = transaction.transacBy
            transacTo = transaction.transacTo
            amountSent = transaction.amountSent

            if min_send <= amountSent <= max_send:
                rewardAmountToSender = int(amountSent * 0.3)

                tUserS1 = User.objects.get(username=transacTo)
                tUserAboutUPI = userInfo.objects.get(ofUser=tUserS1)

                pair = Pair.objects.create(
                    receiver=transacTo,
                    toSend=amountSent,
                    receiverUPI=tUserAboutUPI.UPI
                )
                pair.sender.add(transacBy)

                transaction.rewardAmountToSender = rewardAmountToSender
                transaction.save()

                pairing_info = {
                    'sender_username': transacBy.username,
                    'receiver_username': transacTo.username,
                    'amount_sent': amountSent,
                    'reward_amount_to_sender': rewardAmountToSender,
                    'transaction_date': transaction.datetime.strftime("%Y-%m-%d")
                }
                pairings.append(pairing_info)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

    return HttpResponse(pairings)


def randomize(my_list):
    num_random_values = 3

    if num_random_values > len(my_list):
        num_random_values = len(my_list)

    seed = int(time.time())
    random_values = []

    for _ in range(num_random_values):
        seed = (seed * 9301 + 49297) % 233280
        index = seed % len(my_list)
        random_values.append(my_list.pop(index))

    return random_values[random.choice([0, 1, 2])]


def clearPairs(request):
    try:
        Pair.objects.all().delete()

        return redirect('admin')
    except Exception as e:
        return JsonResponse({"error": e})


def PerformConfirm(request):
    pass
