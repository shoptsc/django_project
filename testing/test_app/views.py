from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')

def customer(request):
    return render(request, 'accounts/customer.html')