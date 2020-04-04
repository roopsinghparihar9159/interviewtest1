from django.http import HttpResponse,Http404
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm 
from .filters import UserFilter
from django.core.paginator import Paginator


def home(request):
    posts = Employee.objects.all()
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context={
    'title':'Insert Record Form',
    'posts':posts,
    'loop_age':range(1,100),
    }
    return render(request,'index.html',context)

def our_view(request):
    if request.POST.get('submit') == 'Add':
        emp(request, format=None)
        return redirect('/')
    elif request.POST.get('submit') == 'Search':
        search(request, format=None)
        return redirect('/')
    else:
        raise Http404()

    return render(request,'index.html')

def emp(request,*args, **kwargs):
    
    if request.method =='POST':

        name = request.POST['name']
        pannumber = request.POST['pannumber']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        city = request.POST['city']

        if Employee.objects.filter(pannumber=pannumber).exists():
            messages.info(request,"Pan Number Already Exists")
            return redirect('/')

        elif Employee.objects.filter(email=email).exists():
            messages.info(request,"Email Already Exists")
            return redirect('/')
        else:
            employee = Employee(name=name,pannumber=pannumber,age=age,gender=gender,email=email,city=city)
            employee.save()
            messages.info(request,"Record Inserted")
        return redirect('/')
    else:
        return render(request,'index.html')

def search(request,*args, **kwargs):
    emp_list = Employee.objects.all()
    emp_filter = UserFilter(request.GET, queryset=emp_list)
    return render(request, 'index.html', {'filter': emp_filter})

def edit(request, id):
    employee = Employee.objects.get(id=id) 
    context={
        'title':'Update Form',
        'employee':employee,
    }
     
    return render(request,'edit.html',context)

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")