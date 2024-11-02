from django.shortcuts import render,redirect
from myApp.models import student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home(req):
    data=student.objects.all()
    if req.method=="POST":
        name=req.POST.get('n')
        dep=req.POST.get('de')
        roll=req.POST.get('r')
        iamge=req.FILES.get('imge')

        obj=student()
        obj.name=name
        obj.dep=dep
        obj.roll=roll
        obj.image=iamge
        obj.save()


    
    return render(req,'index.html',{'d':data})

# sinUp section/ Authentication section start
def sinup(req):
    
    return render(req,'home.html')

def sinUpF(req):

    if req.method=="POST":
        name=req.POST.get('n')
        email=req.POST.get('e')
        username=req.POST.get('u')
        password=req.POST.get('p')
       
        obj=User()
        obj.first_name=name
        obj.email=email
        obj.username=username
        obj.set_password(password)
        obj.save()

        return redirect('LogF')
    return render(req,'sinupForm.html')

def LoginF(req):
    if req.method=="POST":
        username=req.POST.get('u')
        password=req.POST.get('p')
       
        user = authenticate(username=username, password=password)
        
        if user is None:
            return redirect('LogF')
        else:
            login(req, user)
            return redirect('h')
    
   
    return render(req, 'loginForm.html')

    
   



# Delete section

def delItem(req, pk):
    data=student.objects.get(id=pk)
    data.delete()

    return redirect('h')
    

# update section
def upItem(req,pk):
    data=student.objects.get(id=pk)
    if req.method=="POST":
        name=req.POST.get('n')
        dep=req.POST.get('de')
        roll=req.POST.get('r')
        iamge=req.FILES.get('imge')

        obj=student()
        obj.id=pk
        obj.name=name
        obj.dep=dep
        obj.roll=roll
        obj.image=iamge
        obj.save()


        return redirect('h')
    return render(req,'update.html',{'d':data})
