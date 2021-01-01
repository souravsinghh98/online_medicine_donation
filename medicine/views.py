from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import DonateForm, CreateUserForm, CreateNgoForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
# Create your views here.
def donor_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                Donor.objects.create(
                    uname = user
                )
                messages.success(request,'Donor added!!!')
                return redirect('donor_login')
        context = {'form':form}
        return render(request,'medicine/donor_register.html', context)  

def ngo_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateNgoForm()
        if request.method == 'POST':
            form = CreateNgoForm(request.POST)
            if form.is_valid():
                user = form.save()
                NGO.objects.create(
                    uname = user
                )
                messages.success(request,'NGO added!!!')
                return redirect('ngo_login')
        context = {'form':form}
        return render(request,'medicine/ngo_register.html', context)

def donor_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            uname = request.POST['uname']
            pwd = request.POST['pwd']
            user = authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('donor_home')
            else:
                messages.error(request, 'Invalid username or password')    
    return render(request,'medicine/donor_login.html')    

def ngo_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            uname = request.POST['uname']
            pwd = request.POST['pwd']
            user = authenticate(request, username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('ngo_home')
            else:
                messages.error(request, 'Invalid username or password')    
    return render(request,'medicine/ngo_login.html') 

def signin(request):
    return render(request,'medicine/login.html')

def signup(request):
    return render(request, 'medicine/register.html')


def signout(request):
    logout(request)
    return redirect('home')

def home(request):
    total_donations = Donations.objects.all().count()
    total_donor = Donor.objects.all().count()
    context = {'total_donations':total_donations,'total_donor':total_donor}
    return render(request, 'medicine/dashboard.html', context)

def donor_home(request):
    donor = Donor.objects.get(uname=request.user)
    donations = donor.donations_set.all()
    context = {'donations':donations,'donor':donor}
    return render(request,'medicine/donor_home.html',context)

def ngo_home(request):
    ngo = NGO.objects.get(uname=request.user)
    donations = ngo.donations_set.all()
    context = {'donations':donations}
    return render(request,'medicine/ngo_home.html', context)

def donate(request,pk):
    donor = Donor.objects.get(id=pk)
    form = DonateForm(initial={'donor':donor})
    if request.method == 'POST':
        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_home')
    context = {'form':form}
    return render(request,'medicine/donate.html', context) 

def status_update(request,pk):
    donation = Donations.objects.get(id=pk)
    donation.status = 'Delivered'
    donation.save()
    return redirect('ngo_home')
    



