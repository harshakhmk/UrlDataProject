from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def SignUp(request):
    if  request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['user_name']
        email=request.POST['email']
        password =request.POST['password']
        confirm_password =request.POST['confirm_password']
        
        if password==confirm_password:

            if User.objects.filter(username=username).exists():
                  
                    messages.info(request,"User-name already exists")   
                    return redirect('SignUp')

            elif User.objects.filter(email=email).exists():
                
                messages.info(request,"Email taken") 
                return redirect('SignUp')     
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"Redirecting to Login Page")
                
                return redirect("Signin")
            


        else:
            messages.info(request,"Password not matching")
            return redirect('SignUp')
    
    else :  # For GET request just display form  
       return render(request,"register.html")


def Signin(request):
   
   if request.method=='GET':
       return render(request,"Signin.html")
   else :
      
       username=request.POST['user_name']
       password=request.POST['password']
       #check for user existence 
       user=auth.authenticate(username=username,password=password)

       if user is not None: # valid user
           auth.login(request,user)
           return redirect("/")
       else:
           messages.info(request,"invalid username or password")
           return redirect("Signin")    

def Signout(request):

    auth.logout(request)
    return redirect("/")

def HomePage(request):
    return render(request,"index.html")

# Create your views here.



