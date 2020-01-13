from django.http import HttpResponse
from django.shortcuts import render
import pymysql as ps
def details(request):
    return render(request,'form.html')
def entry(request):
    acc=int(request.GET['acc'])
    first=request.GET['first']
    last=request.GET['last']
    dob=request.GET['dob']
    gen=request.GET['gender']
    email=request.GET['email']
    assign=request.GET['assign']
    validity=request.GET['validity']
    state=request.GET['status']
    password=request.GET['pass']
    pin=int(request.GET['pin'])
    conn=ps.connect(host='localhost',port=3306,user='root',password='123',db='locker')
    cmd=conn.cursor()
    q="insert into customer values({},'{}','{}','{}','{}','{}','{}','{}','{}','{}',{})".format(acc,first,last,dob,assign,validity,gen,email,state,password,pin)
    cmd.execute(q)
    conn.commit()
    return render(request,'form.html')
    conn.close()

def login(request):
    return render(request,'login.html')   

def customerlogin(request):
    a=request.GET['pass']
    conn=ps.connect(host='localhost',port=3306,user='root',password='123',db='locker')
    cmd=conn.cursor()
    r="Select * from customer where password='{}'".format(a)
    cmd.execute(r)
    row=cmd.fetchone()
    if(row==None):
        print("Login failed...")
    else:
        return render(request,'dialpad.html',{})
    conn.close()

def adminregister(request):
    return render(request,'adminregister.html')

def entry2(request):
    adminlog=int((request.GET['adminlog']))
    adminpass=(request.GET['adminpass'])
    conn=ps.connect(host='localhost',port=3306,user='root',password='123',db='locker')
    cmd=conn.cursor()
    s="insert into admin values({},'{}')".format(adminlog,adminpass)
    cmd.execute(s)
    conn.commit()
    return render(request,'adminregister.html')
    conn.close()

def login2(request):
    return render(request,'adminlogin.html')
    
def adminlogin(request):
    b=request.GET['adminpass']
    conn=ps.connect(host='localhost',port=3306,user='root',password='123',db='locker')
    cmd=conn.cursor()
    t="Select * from admin where password='{}'".format(b)
    cmd.execute(t)
    row=cmd.fetchone()
    if(row==None):
        print("Login failed...")
    else:
        return render(request,'adminpanel.html',{})
    conn.close() 

def employeedetails(request):
    return render(request,'formemployee.html')

def entry3(request):
    id=int(request.GET['id'])
    first=request.GET['first']
    last=request.GET['last']
    dob=request.GET['dob']
    gen=request.GET['gender']
    email=request.GET['email']
    register=request.GET['register']
    conn=ps.connect(host='localhost',port=3306,user='root',password='123',db='locker')
    cmd=conn.cursor()
    u="insert into employee values({},'{}','{}','{}','{}','{}','{}')".format(id,first,last,dob,gen,email,register)
    cmd.execute(u)
    conn.commit()
    return render(request,'formemployee.html')
    conn.close()
    


