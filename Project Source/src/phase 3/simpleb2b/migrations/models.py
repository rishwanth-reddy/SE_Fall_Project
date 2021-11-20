from django.db import models
# Developed  by Sri Harsha Nadendla
class sellerregistrationmodel(models.Model):
    name=models.CharField(max_length=100)
    loginid=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=100)
    authkey=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

def _str_(self):
    return self.email



class userregistrationmodel(models.Model):
    name = models.CharField(max_length=100)
    loginid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    authkey = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

def _str_(self):
    return self.email


class uploadprodcutsmodel(models.Model):
    ownername = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    productversion = models.CharField(max_length=100)
    vendorname = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    actionprice = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    features = models.CharField(max_length=100)
    date = models.DateField(max_length=50)
    time = models.TimeField(max_length=50)
    images = models.FileField()


def _str_(self):
    return self.productname







class orderproductsmodel(models.Model):
    name = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=100)
    bankname = models.CharField(max_length=100)
    accountnumber = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(max_length=100)
    time = models.TimeField(max_length=100)
