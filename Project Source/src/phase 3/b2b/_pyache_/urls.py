"""b2b URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import path
from django.conf.urls import url
from simpleb2b.views import index, sellerregistration, seller, adminlogin, adminloginaction, adminbase, \
    viewadminsellerpage, logout, activatesellers, sellerpage, userregistration, user, userpage, activateusers, \
    viewadminuserpage, vieworderedproducts, search, searchresult, accuracy

from seller.views import sellerlogincheck, uploadproducts, sellersearch, sellersearchresult, status, searchstatus
from user import views
from user.views import userlogincheck, viewproducts, orderproduct, usersearch, usersearchresult,userpage

# Developed by Preethi Reddy

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url('',index,name="index"),
    url(r'^index/',index,name="index"),
    url(r'^sellerregistration/',sellerregistration, name="sellerregistration"),
    url(r'^seller/',seller,name="seller"),
    url(r'^sellerlogincheck/',sellerlogincheck,name="sellerlogincheck"),
    url(r'^adminlogin/',adminlogin, name="adminlogin"),
    url(r'^adminloginaction/',adminloginaction, name="adminloginaction"),
    url(r'^adminbase/',adminbase, name="adminbase"),
    url(r'^viewadminsellerpage/',viewadminsellerpage, name="viewadminsellerpage"),
    url(r'^activatesellers/$', activatesellers, name="activatesellers"),
    url(r'^sellerpage/', sellerpage, name="sellerpage"),
    url(r'^userregistration/',userregistration,name="userregistration"),
    url(r'^user/',user,name="user"),
    url(r'^userlogincheck/',userlogincheck,name="userlogincheck"),
    url(r'^userpage/',userpage,name="userpage"),
    url(r'^viewadminuserpage/',viewadminuserpage, name="viewadminuserpage"),
    url(r'^activateusers/$', activateusers, name="activateusers"),
    url(r'^uploadproducts/',uploadproducts,name="uploadproducts"),
    #url(r'^userpage/',userpage,name="userpage"),

    url(r'^viewproducts/',viewproducts,name="viewproducts"),
    url(r'^orderproduct/',orderproduct,name="orderproduct"),
    url(r'^vieworderedproducts/',vieworderedproducts,name="vieworderedproducts"),
    url(r'^search/',search,name="search"),
    url(r'^sellersearch/',sellersearch,name="sellersearch"),
    url(r'^searchresult/',searchresult,name = "searchresult"),
    url(r'^sellersearchresult',sellersearchresult,name="sellersearchresult"),
    url(r'^usersearch/',usersearch,name="usersearch"),
    url(r'^usersearchresult/',usersearchresult,name="usersearchresult"),
    url(r'^accuracy/',accuracy,name="accuracy"),
    url(r'^searchstatus/',searchstatus,name="searchstatus"),
    url(r'^status/',status,name="status"),
    url(r'^logout/', logout, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
