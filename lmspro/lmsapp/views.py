from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from .models import User,Book
from .models import Userdata,BookLending
from .retrival import auth
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth import login as loggin
from django.views.decorators.csrf import csrf_exempt


def home(request):
    
    return render(request,"home.html")
def login(request):
    if request.method=="POST":
        
        mail = request.POST.get('mail')
        mail=mail.lower()
        passw = request.POST.get('pass')
        try:
            user=User.objects.get(pk=mail)
        except:
            return HttpResponse("User does not exists")
        if auth(mail,passw):
            loggin(request,user)
            userdata = Userdata.objects.filter(usermail = mail).first()
            if userdata:
                # booklending = BookLending.objects.filter(user = mail)
                # context={
                #     "user" : userdata,
                #     "book_stu":booklending,
                # }
                # return redirect("/after_login/",context)
                return redirect(reverse('after_login'))
            else:
                context={
                    'user' : user,
                }
                return redirect("/aftersignup/?mail="+mail)
        else:
            return HttpResponse("incorrect password")
    queryset = Book.objects.filter(AccessionNumber=30)
    return render(request,"login.html")
def logout_user(request):
    logout(request)
    return redirect("/login/")
def after_login(request,**kwargs):
    user = request.user
    if user.is_superuser:
        branches = ["CIVIL","EEE","MECH","ECE","CSE","IT","CSM","CSO","CIC","AIML","AID"]
        context={
            "branches":branches,
            "username":Userdata.objects.filter(usermail=user).first(),
        }
        return render(request,"adminhtml/after_login.html",context)

    context = {
        'user':Userdata.objects.filter(usermail=user).first(),
        'book_stu':BookLending.objects.filter(user=user)
    }
    for i in context['book_stu']:
        print(i)
    return render(request,"after_login.html",context)
def signup(request):
    if request.method=="POST":
        password = request.POST.get('passw')
        mail = request.POST.get('mail')
        mail=mail.lower()
        if password:
            data=User.objects.create_user(mail,password)
            data.save()
            try:
                user=User.objects.get(pk=mail)
            except:
                pass
            loggin(request,user)
            return redirect("/aftersignup/?mail="+mail)
    return render(request,"signup.html")
@csrf_exempt
def verify(request):
    if request.method == "POST":
        mail=request.POST.get('mail')
        mail=mail.lower()
        exists,in_data=False,False
        exists=User.objects.filter(email__iexact=mail)
        in_data=Userdata.objects.filter(usermail_id=mail)
        if not exists:
            return JsonResponse({"message":"ok"})
        elif not in_data:
            return JsonResponse({"message":"nodata"})
        else:
            return JsonResponse({"message":"exists"})
    return HttpResponse("inside verify view")
@csrf_exempt
def clear(request):
    if request.method=="POST":
        mail = request.POST.get('mail')
        print(mail)
        User.objects.filter(email=mail).delete()
def aboutus(request):
        return render(request,"About_US.html")
def register(request):
    return render(request,"first_login.html")
def forgot(request):
    if request.method=="POST":
        password = request.POST.get('passw')
        mail = request.POST.get('mail')
        mail=mail.lower()
        if password:
            try:
                user=User.objects.update_password(mail,password)
                return redirect("/login/")
            except:
                return HttpResponse("Please try again")
    return render(request,"forgot.html")
def aftersignup(request):

    if request.method=="GET":
        mail = request.GET.get("mail").upper()
        roll_no = mail.split("@")[0]
        branches = {"01":"CIVIL","02":"EEE","03":"MECH","04":"ECE","05":"CSE","12":"IT","42":"CSM","49":"CSO","47":"CIC","61":"AIML","54":"AID"}
        branch = branches[roll_no[6:8]]
        try:
            libraryid = Userdata.objects.get(usermail=mail).libraryid
        except:
            libraryid=None
        if libraryid:
            return render(request,"aftersignup.html",{"roll_no":roll_no,"branch":branch,"libraryid":libraryid})
        else:
            return render(request,"aftersignup.html",{"roll_no":roll_no,"branch":branch})
    elif request.method=="POST":
        roll_no = request.POST.get("rollnum")
        mail = roll_no+"@vvit.net"
        branch = branches[roll_no[6:8]]
        option = request.POST.get("radio")
        
        if option == "male":
            gender = "👨(M)"
        elif option == "female":
            gender = "👧(F)"
        sec = request.POST.get("section")
        name = request.POST.get("name")
        libraryid = request.POST.get("libraryid")
        user=User.objects.get(email=mail.lower())
        exists = False
        exists = Userdata.objects.filter(usermail=user)
        if not exists:
            Userdata.objects.create(usermail=user,rollnumber=roll_no,gender=gender,section=sec,name=name,libraryid=libraryid,branch=branch)
        else:
            exists.delete()
            Userdata.objects.create(usermail=user,rollnumber=roll_no,gender=gender,section=sec,name=name,libraryid=libraryid,branch=branch)
        context = {
        'user':Userdata.objects.filter(usermail=user).first(),
        'book_stu':BookLending.objects.filter(user=user)
            }
        return render(request,"after_login.html",context=context)
    return render(request,"aftersignup.html")
def branch_students(request,branch):
    # branch = request.POST.get("branch")
    print(branch)
    students = Userdata.objects.filter(branch__iexact = branch)
    for student in students:
        print("hi",student.rollnumber)
    context={
        "students": students,
    }
    return render(request,"adminhtml/branch_students.html",context)