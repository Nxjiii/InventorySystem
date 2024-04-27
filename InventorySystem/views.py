from django.shortcuts import render, redirect
from .models import Hardware

APP_NAME = 'InventorySystem/'

def LoginRegister(request):
    return render(request, 'InventorySystem/Logreg.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')

def equipmentList(request):
    # Retrieve items from hardware
    hardware_list = Hardware.objects.all()

    # Filter based on availability
    availability = request.GET.get('availability')
    if availability:
        hardware_list = hardware_list.filter(Status=availability)

    # Search function
    search_query = request.GET.get('search')
    if search_query:
        hardware_list = hardware_list.filter(DeviceName__icontains=search_query)

    # Sort by based on selected option
    sort_by = request.GET.get('sort_by')
    if sort_by:
        if sort_by == 'Quantity':
            hardware_list = hardware_list.order_by('Quantity', 'DeviceName')
        elif sort_by == 'DeviceName':
            hardware_list = hardware_list.order_by('DeviceName', 'Quantity')

    context = {'hardware_list': hardware_list}
    return render(request, 'InventorySystem/Equipment.html', context)




