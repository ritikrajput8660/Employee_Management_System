from django.shortcuts import render,redirect
from app.models import *
# Create your views here.

def homePage(request):
    emp = Emp.objects.all()
    return render(request,'app/home.html',{'emp':emp})
def add_Emp(request):
    if request.method=="POST":
        empId = request.POST['Id']
        empName = request.POST['name']
        empMail = request.POST['mail']
        empPhone = request.POST['phone']

        E = Emp()
        E.EmpId = empId
        E.EmpName = empName
        E.EmpMail = empMail
        E.EmpPhoneNumber = empPhone
        E.save()
        return redirect("/home")

    return render(request,'app/add_Emp.html')


def delete_Emp(request,id):
    E = Emp.objects.get(pk=id)
    E.delete()
    return redirect("/home")


def update_Emp(request,id):
    if request.method=="POST":
        empId = request.POST['Id']
        empName = request.POST['name']
        empMail = request.POST['mail']
        empPhone = request.POST['phone']

        edit = Emp.objects.get(pk=id)
        edit.EmpId=empId
        edit.EmpName=empName
        edit.EmpMail=empMail
        edit.EmpPhoneNumber=empPhone
        edit.save()
        return redirect('/home')
    emp = Emp.objects.get(pk=id)
    context = {'emp':emp}
    print(context)
    return render(request,'app/update_emp.html' ,context)








