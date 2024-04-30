from django.shortcuts import render, redirect
from .models import *




APP_NAME = 'InventorySystem/'


def AdminInventory(request):
   
    items = Electronic_Hardware.objects.all()

    return render(request, 'InventorySystem/AdminInventory.HTML', {'items': items})


def LoginRegister(request):
    return render(request, 'InventorySystem/Logreg.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')

def AdminHomepage(request):
    return render(request, 'InventorySystem/AdminHomepage.HTML')


def AdminManage(request):
    bookings = Hire_Reference.objects.all()
    if request.method == 'POST':
        if 'booking_delete' in request.POST:
            booking_id = request.POST['booking_delete']
            Hire_Reference.objects.filter(id=booking_id).delete()
    return render(request, 'InventorySystem/AdminManage.HTML', {'bookings': bookings})

def AdminReport(request):
    bookings = Hire_Reference.objects.all()
    return render(request, 'InventorySystem/AdminReport.HTML', {'bookings': bookings})

<<<<<<< Updated upstream
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

=======
>>>>>>> Stashed changes
