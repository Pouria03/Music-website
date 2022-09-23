from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .forms import RegisterUserForm
from .models import User
from django.contrib.auth.hashers import make_password


# Create your views here.

class UserRegisterView(View):
    template_name = 'accounts/sign-up.html'
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
            messages.success(request,'your account successfully created')
            return redirect('home:home')
        return render(request,self.template_name,{'form':form})