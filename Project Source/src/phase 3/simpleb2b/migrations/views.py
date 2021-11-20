
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
def searchresult(request):
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')
    print('FRom Date',fromdate, ' and its type ',type(fromdate))
    print('ToDate', todate, ' and its type ', type(todate))
    cnvdate = datetime.strptime(fromdate, '%Y-%m-%d')
    todate = datetime.strptime(todate, '%Y-%m-%d')
    dict = {}
    selldict = {}
    profitdict = {}
    #print('Date Time ',type(cnvdate))
    #today = datetime.date.today()
    check = orderproductsmodel.objects.all().filter(date__range=[cnvdate,todate])
    #print(check)

    object = check.values('productname').distinct()
    #print('Getting Object ',object)

    for x in object:
        y = 0
        z = 0
        amount = 0
        val = orderproductsmodel.objects.filter(productname=x['productname']).aggregate(Sum('amount'))

        y = y+val['amount__sum']
        #print('Val is ',val)
        dict.update({x['productname']:val['amount__sum']})
        #print("val",val['amount__sum'])
        #print(dict)
        val = uploadprodcutsmodel.objects.filter(productname=x['productname']).aggregate(Sum('actionprice'))
        qnty = orderproductsmodel.objects.filter(productname=x['productname']).count()
        z = (z+val['actionprice__sum'])*qnty
        selldict.update({x['productname']:val['actionprice__sum']})
        amount = y-z
        print('Profit Ammount ',amount)
        profitdict.update({x['productname']:amount})
        amount = 0

        #if(y > z):
            #amount = y - z
            #print("amout loss",amount)
    #print('Sell Dict ',selldict)
    #print('Dict ',dict)
    fdict = {}
    for x in dict:
        quantity = orderproductsmodel.objects.filter(productname=x).count()
        sellingprice = dict[x]
        actionprice = selldict[x]
        profit = profitdict[x]
        var = "Seling Price = "+str(sellingprice)+' Action Price = '+str(actionprice)+' Profit ='+str(profit)+' Quantity = '+str(quantity)
        fdict.update({x:var})
    #print(fdict)
    #return render(request,'admins/searchresult.html', {"obj1":dict,"object":check,'totalprice':y,'profit':profitdict})

    #print("Katti ",fdict)
    return render(request, 'admins/searchresult.html',{'objects':fdict,'totalprice':y})



def search(request):
    return render(request,'admins/search.html',{})


def accuracy(request):
    dict =""
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "b2b"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT price FROM simpleb2b_uploadprodcutsmodel")
    myresult = mycursor.fetchall()
    dataset = pd.DataFrame(myresult)
    mycursor.execute("SELECT price FROM simpleb2b_uploadprodcutsmodel")
    myresult1 = mycursor.fetchall()
    dataset1 = pd.DataFrame(myresult1)
    dataset.shape
    X = dataset
    y = dataset1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    m = confusion_matrix(y_test, y_pred)
    accurancy = classification_report(y_test, y_pred)
    print(m)
    print(accurancy)
    x = accurancy.split()
    print("Toctal splits ", len(x))
    dict = {

        "m": m,
        "accurancy": accurancy,
        'len0': x[0],
        'len1': x[1],
        'len2': x[2],
        'len3': x[3],
        'len4': x[4],
        'len5': x[5],
        'len6': x[6],
        'len7': x[7],
        'len8': x[8],
        'len9': x[9],
        'len10': x[10],
        'len11': x[11],
        'len12': x[12],
        'len13': x[13],
        'len14': x[14],
        'len15': x[15],
        'len16': x[16],
        'len17': x[17],
        'len18': x[18],
        'len19': x[19],
        'len20': x[20],
        'len21': x[21],
        'len22': x[22],
        'len23': x[23],
        'len24': x[24],
        'len25': x[25],
        'len26': x[26],
        'len27': x[27],
        'len28': x[28],
        'len29': x[29],
        'len30': x[30],
        'len31': x[31],
        'len32': x[32],
        'len33': x[33],
        'len34': x[34],
        'len35': x[35],
        'len36': x[36],
        'len37': x[37],
        'len38': x[38],
        'len39': x[39],
        'len40': x[40],
        'len41': x[41],
        'len42': x[42],
        'len43': x[43],

    }
    return render(request,'admins/accuracy.html',dict)
