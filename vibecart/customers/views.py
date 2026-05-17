from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Customer
# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('Home')

def show_account(request):
    context={}
    if request.method == 'POST' and 'register' in  request.POST :
        context['register']=True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')   
            password = request.POST.get('password')
            address = request.POST.get('address')   
            phone = request.POST.get('phone')
            # creates user account
            user = User.objects.create_user(username=username, 
                                            email=email, 
                                            password=password)
            # creates customer account
            Customer.objects.create(user=user, 
                                    name=username, 
                                    address=address, 
                                    phone=phone)
            sucess_message = "Account created successfully! Please login to continue."
            messages.success(request, sucess_message)
        except Exception as e:
            error_message = "Username already exists. Please choose a different username. "
            messages.error(request, error_message)
    if request.method == 'POST' and 'login' in  request.POST :
        context['register']=False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request,'account.html')