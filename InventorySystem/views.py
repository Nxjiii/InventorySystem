from django.shortcuts import render, redirect

APP_NAME = 'InventorySystem/'

def LoginRegister(request):
    return render(request, 'InventorySystem/Logreg.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')

def AdminHomepage(request):
    return render(request, 'InventorySystem/AdminHomepage.HTML')

def AdminInventory(request):
    return render(request, 'InventorySystem/AdminInventory.HTML')

def AdminManage(request):
    return render(request, 'InventorySystem/AdminManage.HTML')

def AdminBookings(request):
    return render(request, 'InventorySystem/AdminBookings.HTML')
