from django.shortcuts import render,redirect
from E_Farm.models import Farmer,Consumer,Product
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth


# Create your views here.
def home(request):
    p = Product.objects.all()

    return render(request,"home.html",{"p":p})

def farmerReg(request):
    if request.method=="POST":
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        Mob = request.POST.get("Mob")
        Email = request.POST.get("Email")
        Pass1 = request.POST.get("Pass1")
        Pass2 = request.POST.get("Pass2")
        print(Fname,Lname,Mob,Email,Pass1,Pass2)
        f = Farmer()
        f.fname = Fname
        f.lname = Lname
        f.femail = Email
        f.pass1 = Pass1
        f.pass2 = Pass2
        f.phone = Mob
        f.save()
        user = User.objects.create_user(username=Email,password=Pass1)
        user.save()
        #messages.success(request,"Your Account has been Successfully  created :-)")
        return redirect("/farmer-login/")
    return render(request,"f_reg.html")

def farmerLog(request):
    if request.method=="POST":
        Email = request.POST.get("email")
        Pass = request.POST.get("password")
        type = request.POST.get("type")
        print(Email,Pass,type)
        u = auth.authenticate(username=Email,password=Pass)
        print(u)
        if u is not None:
            auth.login(request,u)
            print("p1")
            return redirect("/add-product/")
        #if Farmer.objects.get(Email=Email).exist():  
        else:
            print("p2")
            return render(request,"login.html")
    return render(request,"login.html")

def userReg(request):
    if request.method=="POST":
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        Email = request.POST.get("Email")
        Pass1 = request.POST.get("Pass1")
        Pass2 = request.POST.get("Pass2")
        Gender = request.POST.get("Gender")
        Phone = request.POST.get("Phone")
        Address = request.POST.get("Address")
        print(Fname,Lname,Email,Pass1,Pass2,Phone,Gender,Address)
        #return HttpResponse("<h1>Welcome to Home Page1</h1>")
        c = Consumer()
        c.fname = Fname
        c.lname = Lname
        c.cemail = Email
        c.pass1 = Pass1
        c.pass2 = Pass2
        c.phone = Phone
        c.address = Address
        if Gender=="male":
            c.gender = 'M'
        elif Gender=="female":
            c.gender = "F"
        else:
            c.gender = "O"
        c.save()
        user = User.objects.create_user(username=Email,password=Pass1)
        user.save()
        #messages.success(request,"Your Account has been Successfully  created :-)")
        return redirect("/user-login/")
    return render(request,"user_reg.html")

def addPro(request):
    if request.method=="POST":
        Pname = request.POST.get("Pname")
        Pprice = request.POST.get("Pprice")
        Pquality = request.POST.get("Pquality")
        Pquantity = request.POST.get("Pquantity")
        Pimage = request.POST.get("Pimage")
        print(Pname,Pprice,Pquality,Pquantity,Pimage)
        """p = Product()
        p.pname = Pname
        p.pprice = Pprice
        p.pquality = Pquality
        p.pquantity = Pquantity
        p.pimage = Pimage
        p.save()"""
    return render(request,"addProduct.html")

def userLog(request):
    if request.method=="POST":
        Email = request.POST.get("email")
        Pass = request.POST.get("password")
        type = request.POST.get("type")
        print(Email,Pass,type)
        if type=="consumer":
            u = auth.authenticate(username=Email,password=Pass)
            print(u)
            if u is not None:
                auth.login(request,u)
                print("p1")
                return redirect("/")
            #if Farmer.objects.get(Email=Email).exist():  
            else:
                print("p2")
                return render(request,"login.html")
        else:
            pass
    return render(request,"login.html")

def aboutUs(request):
    return render(request,"aboutUs.html")

def contactUs(request):
    return render(request,"contactUs.html")