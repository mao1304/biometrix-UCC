from django import forms
from .models import NewUser
 
class NewUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = {'username', 'password', 'first_name', 'last_name','huella', 'admin_check',}
        
class LoginUserForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = {'username', 'password',}
                
class AdminUserForm(forms.ModelForm):
    class Meta:
        model = NewUser 
        fields = {'username', 'password', 'admin_check',}  
 