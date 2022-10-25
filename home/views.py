from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from . import forms
from .models import ContactUs
# 

class HomeView(View):
    def get(self,request):
        return render(request,'home/home.html')


class ContactUsView(View):
    template_name = 'home/contactUs.html'
    form_class = forms.ContactUsForm
    
    def dispatch(self, request, *args, **kwargs) :
        if not request.user.is_authenticated:
            messages.warning(request,'you must login to your account','warning')
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            ContactUs.objects.create(contact_type=form.cleaned_data['contact_type'],
            request=form.cleaned_data['request'],user=request.user.email
            )
            messages.success(request,'your message sent to admins','success')
            return redirect('home:home')

        return render(request,self.template_name,{'form':form})