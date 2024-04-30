from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist




APP_NAME = 'InventorySystem/'

def profile(request):
    return render(request, 'InventorySystem/profile.HTML')



def AdminInventory(request):

    items = Electronic_Hardware.objects.all()

    return render(request, 'InventorySystem/AdminInventory.HTML', {'items': items})


def LoginRegister(request):
    return render(request, 'InventorySystem/Logreg.HTML')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('AdminManage')
        else:
            return render(request, 'InventorySystem/Logreg.HTML', {'error': 'Invalid email or password'})

def AdminLogout(request):
    return redirect('LoginRegister')

def AdminUser(request):
    users = User.objects.all()
    print('users', users)
    return render(request, 'InventorySystem/AdminUser.HTML', {'users': users})

def delete_user(request):
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        print('user_id', user_id)
        try:
            user = User.objects.get(id=user_id)
            user.delete() 
        except ObjectDoesNotExist:
            print(f"No user with ID {user_id} exists.") 
        return redirect('AdminUser')
    else: 
        return redirect('AdminUser')


def AdminManage(request):
    bookings = Hire_Reference.objects.all()
    return render(request, 'InventorySystem/AdminManage.HTML', {'bookings': bookings})

def delete_booking(request):
    
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = Hire_Reference.objects.get(id=booking_id)
        booking.delete()  
        return redirect('AdminManage')

def AdminReport(request):
    bookings = Hire_Reference.objects.all()
    return render(request, 'InventorySystem/AdminReport.HTML', {'bookings': bookings})

def AdminBookings(request):
    return render(request, 'InventorySystem/AdminBookings.HTML')


def UserInventory(request):
    Electronic_items = Electronic_Hardware.objects.all()
    Hardware_items = Hardware.objects.all()
    return render(request, 'InventorySystem/UserInventory.HTML', {'electronics': Electronic_items, 'Hardware': Hardware_items})

def UserInventory(request):
    device_type = request.GET.get('deviceType')  # Get the selected device type from the request

    if device_type:  
        electronic_items = Electronic_Hardware.objects.filter(DeviceType=device_type)
        hardware_items = Hardware.objects.filter(DeviceType=device_type)
    else:  # If no device type is selected, return all items
        electronic_items = Electronic_Hardware.objects.all()
        hardware_items = Hardware.objects.all()

    return render(request, 'InventorySystem/UserInventory.HTML', {'electronics': electronic_items, 'Hardware': hardware_items, 'selected_device_type': device_type})

