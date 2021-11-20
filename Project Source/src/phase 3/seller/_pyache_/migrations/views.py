from datetime import datetime

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render,redirect

from simpleb2b.forms import uploadform
from simpleb2b.models import sellerregistrationmodel, uploadprodcutsmodel
from django.contrib import messages

# Developed by Roja Kamble
def sellerlogincheck(request):
    if request.method=='POST':
        usid=request.POST.get('loginid')
        pswd=request.POST.get('password')
        try:
            check =sellerregistrationmodel.objects.get(loginid=usid,password=pswd)
            request.session['ownid'] = check.loginid
            request.session['loggeduser'] = check.name
            status=check.status
            if status=="activated":
                request.session['email']=check.email
                return render(request,'seller/sellerpage.html')
            else:
                messages.success(request,'seller is not activated')
                return render(request,'seller/seller.html')
            return render(request,'seller/seller.html')
        except Exception as e:
            print('Exception is',str(e) )
            messages.success(request,'Invalid ID and Password')
        return render(request,'seller/seller.html')


def uploadproducts(request):
    if request.method == "POST":
        form = uploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'product upload successfully ')
            return redirect('seller.html')
    else:
        form = uploadform()
    return render(request,'seller/uploadproducts.html',{'form': form})



def searchstatus(request):

    return render(request,'seller/searchstatus.html',{})



def status(request):
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')
    print('FRom Date', fromdate, ' and its type ', type(fromdate))
    print('ToDate', todate, ' and its type ', type(todate))
    print(todate)
    cnvdate = datetime.strptime(fromdate, '%Y-%m-%d')
    todate = datetime.strptime(todate, '%Y-%m-%d')
    dict = {}
    print('Date Time ', type(cnvdate))
    object = uploadprodcutsmodel.objects.filter(date__range=[cnvdate, todate])
    return render(request, 'seller/status.html', {'object': object})


def sellersearch(request):

    return render(request,'seller/sellersearch.html',{})



def sellersearchresult(request):
    fromdate = request.GET.get('fromdate')
    todate = request.GET.get('todate')
    print('FRom Date', fromdate, ' and its type ', type(fromdate))
    print('ToDate', todate, ' and its type ', type(todate))
    print(todate)
    cnvdate = datetime.strptime(fromdate, '%Y-%m-%d')
    todate = datetime.strptime(todate, '%Y-%m-%d')
    dict = {}
    print('Date Time ', type(cnvdate))
    check =  uploadprodcutsmodel.objects.filter(date__range=[cnvdate, todate])
    print(check)
    current_ownid =  request.session['ownid']
    print(current_ownid)
    ownername = request.session['ownid']
    object = check.filter(ownername=ownername)
    #dict=uploadprodcutsmodel.objects.all()
    return render(request, 'seller/sellersearchresult.html',{'object':object})





