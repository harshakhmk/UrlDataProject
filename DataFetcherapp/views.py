from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
import requests,json,urllib.request
from .models import URLData
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError





# Create your views here.
def form_page(request):

        if request.method=='GET': 
           
              return render(request,"form_page.html")
              
        
        else :
         if request.user.is_authenticated :   
           url=request.POST['url'] 
           req_object=Request(url)
           with urllib.request.urlopen(req_object) as response:
                myfile = response.read()
        
            #f = urllib.request.urlopen(url)
            #myfile = f.read()
           obj=URLData(url=url,user=request.user,data=myfile)
           obj.save()
           context={
                  "Data":myfile
                 } 
           return render(request,"data_display.html",context)
         else:
             messages.info(request,"Redirected to Home page since,User didn't Login")
             return redirect("/")
# Create your views here.
