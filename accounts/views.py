from re import TEMPLATE
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterUserForm, UserLoginForm
from .models import User
from django.contrib.auth.hashers import make_password


# Create your views here.

class UserRegisterView(View):
    template_name = 'accounts/signup.html'
    form_class = RegisterUserForm
    
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(email=data['email'].strip()
            ,password=make_password(data['password1']))
            # 
            # permissions and group and accesses
            messages.success(request,'your account successfully created . please LOG IN')
            return redirect('accounts:login')
        return render(request,self.template_name,{'form':form})


class UserLoginView(View):
    template_name = 'accounts/login.html'
    form_class    = UserLoginForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['email'],password=data['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'wellcome to MusicOnline !!','success')
                return redirect('home:home')
            else:
                messages.warning(request,'this email or password is not valid','warning')
                return render(request,self.template_name,{'form':form})
        return render(request,self.template_name,{'form':form})

class UserLogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        logout(request)
        messages.success(request,'you successfully logged out','success')
        return redirect('home:home')