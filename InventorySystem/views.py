from django.shortcuts import render, redirect

APP_NAME = 'InventorySystem/'

def Adtemp(request):
    return render(request, 'InventorySystem/AdminTemplate.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')



