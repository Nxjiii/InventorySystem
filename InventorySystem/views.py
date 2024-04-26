from django.shortcuts import render, redirect
from .models import Hardware

APP_NAME = 'InventorySystem/'

def LoginRegister(request):
    return render(request, 'InventorySystem/Logreg.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')

def equipmentList(request):
    hardware_list = Hardware.objects.all()
    
    
    context = {'hardware_list': hardware_list}
    return render(request, 'InventorySystem/UserTemplate.HTML', context)



