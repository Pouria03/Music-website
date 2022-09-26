from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User
# =================================================================

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(
        help_text="you can change password using <a href=\"../password/\">this form</a>."
        )

    class Meta:
        model = User
        fields = ('email', 'password','is_active','is_admin','is_pro')

# ============================================================================

class RegisterUserForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(),label='password')
    password2 = forms.CharField(widget=forms.PasswordInput(),label='confirm password')

    def clean_email(self):
        email = self.cleaned_data['email']
        email = email.strip()
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise ValidationError('please enter onother email, this email is already exists')
        return email

            
    def clean(self):
        cleaned_data = super().clean()
        password1 =  cleaned_data.get('password1')
        password2 =  cleaned_data.get('password2')

        if password1 and password2 and password1 != password2 :
            raise ValidationError('passwords must match')
        
        if password1 and len(password1) < 4 :
            raise ValidationError('password must be morethan 4 characters')
        

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    

class GetPremiumForm(forms.Form):
    paied = forms.BooleanField()
