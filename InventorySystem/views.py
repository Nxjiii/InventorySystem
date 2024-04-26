from django.shortcuts import render, redirect

APP_NAME = 'InventorySystem/'

def LoginRegister(request):
    return render(request, 'InventorySystem/Logreg.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')

def Admin(request):
    return render(request, 'InventorySystem/AdminHomepage.HTML')
