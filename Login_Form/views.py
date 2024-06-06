from django.shortcuts import render,redirect
import mysql.connector
from .models import Create_Acc
# Create your views here.


def Home(request):
    return render(request,"home.html")

def Create_Accs(request):
    if request.method == "GET":
        return render(request, "Create_ACC.html")
    else:
        try:
            name = request.POST.get('name')
            password = request.POST.get('ps')
            email_id = request.POST.get('em')
            mobile=request.POST.get('mb')
            obj = Create_Acc(Name=name, Password=password, Email_id=email_id,Mobile=mobile)
            obj.save()
            return render(request, 'Create_ACC.html',{'Result':'Account Created Successfully'})
        except Exception as ex:
            return render(request, 'Create_ACC.html',{'Result':ex})


def login(request):
    if request.method== "GET":
        return render(request,"Login.html")
    else:
        try:
            email=request.POST.get('email')
            password=request.POST.get('password')
            obj=Create_Acc.objects.filter(Email_id=email,Password=password).values()
            if (len(obj)>0):
                return render(request,'welcome.html')
            else:
                return render(request,'login.html',{'message2':'Incorrect password & Email_Id'})
        except Exception as ex:
            return render(request,'login.html',{'message':ex})



def change_password(request):
    if request.method=='GET':
        return render(request,'change_password.html')
    else:
        pass
def logout(request):
    return render(request,'Login.html',{'message':'Logout Successfully'})