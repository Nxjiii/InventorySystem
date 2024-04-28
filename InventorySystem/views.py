from django.shortcuts import render, redirect
from .models import Hardware, Electronic_Hardware


APP_NAME = 'InventorySystem/'


def AdminInventory(request):
    # Retrieve all items from the Electronic_Hardware model
    items = Electronic_Hardware.objects.all()
    # Pass the items to the template for rendering
    return render(request, 'InventorySystem/AdminInventory.HTML', {'items': items})


def LoginRegister(request):
    return render(request, 'InventorySystem/Logreg.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')

def AdminHomepage(request):
    return render(request, 'InventorySystem/AdminHomepage.HTML')


def AdminManage(request):
    return render(request, 'InventorySystem/AdminManage.HTML')

def AdminBookings(request):
    return render(request, 'InventorySystem/AdminBookings.HTML')
