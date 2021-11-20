from django import forms
from simpleb2b.models import sellerregistrationmodel, userregistrationmodel, uploadprodcutsmodel, \
    orderproductsmodel

# Developed by Neha Geereddy
class sellerregistrationform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    loginid=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    password=forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email=forms.EmailField(widget=forms.TextInput(), required=True)
    contact=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    authkey=forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status=forms.CharField(widget=forms.HiddenInput(),initial='waiting', max_length=100)

    class Meta:
        model= sellerregistrationmodel
        fields=['name','loginid','password','email','contact','authkey','status']


class userregistrationform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=100)
    email = forms.EmailField(widget=forms.TextInput(), required=True)
    contact = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    authkey = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta:
        model=userregistrationmodel
        fields=['name','loginid','password','email','contact','authkey','status']





class uploadform(forms.ModelForm):
    ownername = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    productname=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    vendorname = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    productversion = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    color = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    actionprice = forms.CharField(widget=forms.NumberInput(), required=True, max_length=100)
    price = forms.CharField(widget=forms.NumberInput(),required=True,max_length=100)
    features = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    date = forms.DateField(widget=forms.DateInput())
    time = forms.TimeField(widget=forms.TimeInput())
    images = forms.FileField(widget=forms.FileInput())
    class Meta:
        model = uploadprodcutsmodel
        fields = ('ownername','productname','vendorname','productversion','color','actionprice','price','features','date','time','images')










class orderproductsform(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}),required=True,max_length=100)
    productname = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}),required=True,max_length=100)
    address = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    mobilenumber = forms.CharField(widget=forms.NumberInput(),required=True,max_length=100)
    bankname = forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
    accountnumber = forms.CharField(widget=forms.NumberInput(),required=True,max_length=100)
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'readonly'}),required=True)
    date = forms.DateField(widget=forms.DateInput())
    time = forms.TimeField(widget=forms.TimeInput())

    class Meta:
        model = orderproductsmodel
        fields = ('name','productname','address','mobilenumber','bankname','accountnumber','amount','date','time')
