from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from .models import *
from transactionControl.models import Transaction, Confirmed

import uuid
from datetime import datetime

# Create your views here.


def index(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, 'authenticate-user.html')
        else:
            return redirect('home')
    else:
        if request.POST['type'] == "signup":
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            upi = request.POST['upi']
            referredByUser = request.POST['refID']

            referrerID = uuid.uuid1()

            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.add_message(
                    request, messages.ERROR, 'User with given email/username already exists')

                return redirect('/a')
            else:
                if not userInfo.objects.filter(UPI=upi).exists():
                    try:
                        newUser = User.objects.create_user(
                            email=email, username=username, password=password)
                        newUser.save()

                        user_id = newUser.pk
                        username = newUser.username

                        aboutUser = userInfo(
                            ofUser=newUser, UPI=(upi), userReferralID=str(referrerID).upper())

                        aboutUser.save()

                        d = datetime.now()

                        first_transaction = Transaction(
                            transacBy=newUser, transacTo=User.objects.get(id=20), amountSent=1000, rewardAmountToSender=0, datetime=d.date())
                        first_transaction.save()

                        confirm = Confirmed(
                            transaction=first_transaction, confirmed=True)
                        confirm.save()

                        if len(referredByUser.replace(" ", "")) != 0:
                            referenceByS1 = userInfo.objects.get(
                                userReferralID=referredByUser)

                            referenceByS2 = User.objects.get(
                                username=referenceByS1.ofUser)

                            references = referredBy(
                                referredByUser=referenceByS2, referredToUser=referrerID)
                            references.save()

                        logUserSU = authenticate(
                            username=username, password=password)

                        if logUserSU is not None:
                            login(request, logUserSU)

                            return redirect('/home')
                        else:
                            messages.add_message(
                                request, messages.ERROR, "Couldn't login")
                            return redirect('/a')
                    except Exception as e:
                        messages.add_message(request, messages.ERROR, str(e))
                        return redirect('/a')
                else:
                    messages.add_message(
                        request, messages.ERROR, "UPI Phone Number Already In Use")

                    return redirect('/a')
        else:
            username = request.POST.get('username_login')
            password = request.POST.get('password_login')

            print(list((username, password)))

            logUser = authenticate(username=username, password=password)

            if logUser is not None:
                login(request, logUser)

                return redirect('/home')
            else:
                messages.add_message(
                    request, messages.ERROR, "Invalid Credentials")

                return redirect('/a')


def logUserOut(request):
    logout(request)

    return redirect('/a')
