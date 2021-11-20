
from datetime import datetime
from random import randint
import mysql.connector
import pandas as pd
from Tools.demo.sortvisu import distinct
#from pg_utils import DistinctSum
from django.db.models import Sum


from django.db.models import Count, Sum
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib import messages
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

from simpleb2b.forms import sellerregistrationform, userregistrationform, uploadform, orderproductsform
from simpleb2b.models import sellerregistrationmodel, userregistrationmodel, uploadprodcutsmodel, orderproductsmodel

# Developed by Meghana Thimmapuram & Sai Nikhil Chitturi
def index(request):
    return render(request,'index.html',{})

def sellerregistration(request):
    if request.method == 'POST':
        form = sellerregistrationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'you are successfully registred')
            return HttpResponseRedirect('seller')
        else:
            print('Invalid')
    else:
        form = sellerregistrationform()
    return render(request,"seller/sellerregistration.html",{'form':form})


def seller(request):
    context={}
    return render(request,'seller/seller.html',context)

def sellerpage(request):
    context = {}
    return  render(request,"seller/sellerpage.html",context)


def adminbase(request):
    return render(request,"adminbase.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def adminloginaction(request):
    if request.method == "POST":
        #if request.method == "POST":
            usid = request.POST.get('username')
            pswd = request.POST.get('password')
            if usid == 'admin' and pswd == 'admin':
                return render(request,'admins/adminhome.html')
            else:
                messages.success(request, 'Invalid user id and password')
    #messages.success(request, 'Invalid user id and password')
    return render(request,'adminlogin.html')

def viewadminsellerpage(request):
    sellerdata = sellerregistrationmodel.objects.all()
    return render(request,'admins/viewsellerdata.html',{'object':sellerdata})


def activatesellers(request):
    if request.method=='GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        sellerregistrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        sellerdata = sellerregistrationmodel.objects.all()
        return render(request,'admins/viewsellerdata.html',{'object':sellerdata})

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def userregistration(request):
    if request.method == 'POST':
        form = userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are successfully registred')
            return HttpResponseRedirect('user')
        else:
            print('Invalid')
    else:
        form = userregistrationform()
    return render(request,"user/userregistration.html",{'form':form})


def user(request):
    context={}
    return render(request,'user/user.html',context)

def userpage(request):
    context = {}
    return  render(request,"user/userpage.html",context)


def activateusers(request):
    if request.method == 'GET':
        usid = request.GET.get('usid')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("USID = ",usid,authkey,status)
        userregistrationmodel.objects.filter(id=usid).update(authkey=authkey , status=status)
        userdata = sellerregistrationmodel.objects.all()
        return render(request,'admins/viewuserdata.html',{'object':userdata})


def viewadminuserpage(request):
    userdata = userregistrationmodel.objects.all()
    return render(request,'admins/viewuserdata.html',{'object':userdata})


def logout(request):
    return render(request,'index.html')

def vieworderedproducts(request):
    dict = orderproductsmodel.objects.all()
    return render(request,'admins/vieworderedproducts.html',{'object':dict})
