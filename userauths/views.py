from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

User = settings.AUTH_USER_MODEL 

# Create your views here.
def register_view(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f'{username}, Your account creted successfully!')
            new_user = authenticate(username = form.cleaned_data['email'],
                                    password = form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("core:index")
    
    else:   
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"userauths/sign-up.html",context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.warning(request,f"User with {email} does not exist")

        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,f"{user} logged in.")
            return redirect("core:index")
        else:
            messages.warning(request,"{user} Does Not Exist, Create an account.")

    context = {}
    return render(request,"userauths/login.html", context)
 

def logout_view(request):
    logout(request)
    messages.warning(request,"You logged out.")

    return redirect("userauths:sign-in")



