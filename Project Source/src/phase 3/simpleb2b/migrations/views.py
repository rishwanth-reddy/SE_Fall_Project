import email
from datetime import time

from django.core.files import images
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from simpleb2b.forms import  orderproductsform
from simpleb2b.models import userregistrationmodel, uploadprodcutsmodel,orderproductsmodel
from django.contrib import messages

# Developed by Divya Kumbham & Rishwanth Reddy

def userlogincheck(request):
    if request.method =='POST':
        usid=request.POST.get('loginid')
        print(usid)
        pswd=request.POST.get('password')
        print(pswd)
        try:
            check = userregistrationmodel.objects.get(loginid=usid,password=pswd)
            request.session['userid'] = check.loginid
            request.session['loggeduser'] = check.name
            status = check.status

            if status == "activated":
                print("User Status Is ", check.email)
                request.session['email'] = check.email
                #print(email)
                #return HttpResponse("User Login Success")
                dict = uploadprodcutsmodel.objects.all()
                return render(request,'user/userpage.html',{'objects':dict})
            else:
                messages.success(request,'user is not activated')
                return render(request,'user/user.html',{})
                #return render(request,'user/userpage.html')
        except Exception as e:
            print('Exception is',str(e) )
            messages.success(request,'Invalid ID and Password')
        return render(request,'user/user.html',{})


def userpage(request):
    products = uploadprodcutsmodel.objects.all()
    print("image=",products.images)
    return render(request,'user/userpage.html',{'products':products})


def viewproducts(request):
    '''dict=uploadprodcutsmodel.objects.all()
    return render(request,'user/viewproducts.html',{'objects':dict})'''
    id = request.GET.get('id')
    check = uploadprodcutsmodel.objects.get(id=id)
    request.session['id'] = check.id
    id = request.session["id"]
    dict = uploadprodcutsmodel.objects.get(id=id)
    return render(request, 'user/viewproducts.html', {'dict': dict})
