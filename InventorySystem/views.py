from django.shortcuts import render, redirect

APP_NAME = 'InventorySystem/'

def signup(request):
    return render(request, 'InventorySystem/Signup.html')

