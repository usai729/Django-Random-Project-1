from django.shortcuts import render, redirect, HttpResponse
from authentication.views import *
from django.contrib.auth.models import User
from authentication.models import *

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        LOGGEDINuserID = request.user.id

        userInfoP1 = userInfo.objects.get(ofUser=LOGGEDINuserID)
        userCore = User.objects.get(id=LOGGEDINuserID)

        signedinUserDetails = {'username': userCore.username, 'email': userCore.email,
                               'dateJoined': userCore.date_joined, 'UPIphnoneNumber': userInfoP1.UPI, 'MyRefCode': userInfoP1.userReferralID}

        return render(request, 'home.html', {'main_user_details': signedinUserDetails})
    else:
        return redirect('/a')


def edit(request):
    typeOfEdit = request.GET['editType']
    newInfo = request.GET['newInfo']

    user_id = request.user.id

    if typeOfEdit == "myemail":
        if User.objects.filter(email=newInfo).exists():
            messages.add_message(request, messages.ERROR,
                                 "Email Already In Use")
        else:
            updateInfoEmail = User.objects.get(id=user_id)
            updateInfoEmail.email = newInfo

            updateInfoEmail.save()
            messages.add_message(request, messages.SUCCESS,
                                 "")
    else:
        if userInfo.objects.filter(UPI=newInfo).exists():
            messages.add_message(request, messages.ERROR,
                                 "UPI Phone Number Already In Use")
        else:
            updateInfoUPI = userInfo.objects.get(ofUser=user_id)
            updateInfoUPI.UPI = int(newInfo)

            updateInfoUPI.save()
            messages.add_message(request, messages.SUCCESS,
                                 "")

    return redirect('/home')


def myprofile(request):
    if not request.user.is_authenticated:
        return redirect('/a')
    else:
        return render(request, 'myprofile.html')


def transactions(request):
    return HttpResponse("Transactions")


def running(request):
    return HttpResponse("Running")


def notifs(request):
    return HttpResponse("Notifications")
