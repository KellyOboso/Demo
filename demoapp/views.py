from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def about(request):
    return render(request, 'about.html')

def accounts(request):
    return render(request, 'accounts.html')

def allmembers(request):
    return render(request, 'allmembers.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    all_data = Transaction.objects.all()
    return render(request, 'index.html',{'key1':all_data})

def loans(request):
    return render(request, 'loans.html')

def LoginPage(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'reg.html')

def RegisterPage(request):
    return render(request, 'register.html')

def settings(request):
    return render(request, 'settings.html')

def single(request):
    return render(request, 'single.html')

def starter(request):
    return render(request, 'starter.html')

def test(request):
    return render(request, 'test.html')

def transactions(request):
    all_data = Transaction.objects.all()
    return render(request, 'transactions.html',{'key1':all_data})

#data insertion from registration page
def UserRegister(request):
    if request.method == "POST":
        idtype = request.POST['idtype']
        idnumber = request.POST['idnumber']
        opendate = request.POST['opendate']
        title = request.POST['title']
        fname = request.POST['fname']
        lname = request.POST['lname']
        birthdate = request.POST['birthdate']
        krapin = request.POST['krapin']
        country = request.POST['country']
        county = request.POST['county']
        residence = request.POST['residence']
        postalcode = request.POST['postalcode']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword'] 

        #validating if user exists
        user = UserRegistration.objects.filter(Email=email)

        if user:
            message = "User already esists. Proceed to Login"
            return render(request, "login.html", {'msg':message})
        else:
            if password == cpassword:
                newuser = UserRegistration.objects.create(Id_Type=idtype,Id_Number=idnumber,Open_Date=opendate,Title=title,
                                                          Firstname=fname,Lastname=lname,Birth_Date=birthdate,Kra_Pin=krapin,
                                                          Country=country,Residence=residence,Postal_Code=postalcode,Mobile=mobile,
                                                          Email=email,Password=password)   
                message = "User Registered Successfuly"
                return render(request,"login.html",{'msg':message})
            else:
                message = "Passwords don't Match"
        return render(request,"register.html",{'msg':message})  

#View for user Login
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        #checking the email id with database
        user = UserRegistration.objects.get(Email=email)

        if user:
            #getting user data in session
            if user.Password == password:
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                request.session['Mobile'] = user.Mobile
                request.session['Title'] = user.Title
                request.session['Password'] = user.Password
                

                message = "User Login Successfull"
                return render(request,"index.html",{'msg':message})
            else:
                message = "Passwords don't match"
                return render(request,"login.html",{'msg':message})
        else:
            message = "User does not exists. Proceed to Register"
            return redirect(request,"register.html",{'msg':message})    

#Contact Page View
def InsertContact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']

        newcontact = Contact.objects.create(Firstname=fname, Lastname=lname ,Email=email
                                         ,Mobile=mobile, Message=message)
        
        return redirect('contact')

#All Members
def AllMembers(request):
    #select * from UserRegistration
    #Fetching Data into Table
    all_data = UserRegistration.objects.all()
    return render(request,'allmembers.html',{'key1':all_data})

#transactions view
def InsertTransactions(request):
    if request.method == "POST":
        transactiontype = request.POST['transactiontype']
        amount = request.POST['amount']
        date = request.POST['date']

        newtransaction = Transaction.objects.create(Transaction_type=transactiontype, Amount=amount, Date=date)

        return redirect ('transactions')
    