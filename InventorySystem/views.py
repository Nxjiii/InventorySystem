from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from .models import Hire_Reference
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required






APP_NAME = 'InventorySystem/'

@login_required
def profile(request):
   
    user = request.user
    bookings = Hire_Reference.objects.filter(Username=user.username)
    return render(request, 'InventorySystem/profile.html', {'user': user, 'bookings': bookings})



def logoutview(request):
    logout(request)  
    return redirect('LoginRegister') 

def create_booking(request):
    if request.method == 'POST':
       
        device_name = request.POST.get('device_name')
        hire_start_date = request.POST.get('hire_start_date')
        hire_end_date = request.POST.get('hire_end_date')

     
        try:
            booking = Hire_Reference.objects.create(
                DeviceName=device_name,
                Hire_StartDate=hire_start_date,
                Hire_EndDate=hire_end_date,
                user=request.user  
            )
      
            return JsonResponse({'success': True})
        except Exception as e:
            
            return JsonResponse({'success': False, 'error': str(e)})

    
    return redirect('profile/')

 











def UserHomepage(request):
    return render(request, 'InventorySystem/UserHomepage.HTML')





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
        
        if user is not None:
            if user.is_staff:  
                login(request, user)
                return redirect('adminman/')  
            else:

                login(request, user)
                return redirect('Inventory/')  
        else:
            return render(request, 'InventorySystem/Logreg.HTML', {'error': 'Invalid email or password'})

    return render(request, 'InventorySystem/Logreg.HTML') 
        




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
    if request.method == 'POST':
        device_name = request.POST.get('device_name')
        if device_name:
        
            booking = Hire_Reference.objects.create(
                RefID=1,  
                Hire_StartDate=timezone.now(),
                Hire_EndDate=timezone.now() + timezone.timedelta(days=20),
                Username=request.user.username,  
                AdminUsername='Admin',  
                HardwareID=device_name,
                Status='Requested'
            )
            return JsonResponse({'success': True})
        else:
          
            return JsonResponse({'success': False, 'error': 'Device name not provided'})

    
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
    device_type = request.GET.get('deviceType') 

    if device_type:  
        electronic_items = Electronic_Hardware.objects.filter(DeviceType=device_type)
        hardware_items = Hardware.objects.filter(DeviceType=device_type)
    else:  
        electronic_items = Electronic_Hardware.objects.all()
        hardware_items = Hardware.objects.all()

    return render(request, 'InventorySystem/UserInventory.HTML', {'electronics': electronic_items, 'Hardware': hardware_items, 'selected_device_type': device_type})

