from django.shortcuts import render, redirect

APP_NAME = 'InventorySystem/'

def AdminDash(request):
    return render(request, 'InventorySystem/AdminDash.HTML')

def User(request):
    return render(request, 'InventorySystem/UserTemplate.HTML')



