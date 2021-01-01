from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class DonateForm(ModelForm):
    class Meta:
        model = Donations
        fields = ['donor','ngo','med_name','expiry_date']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class CreateNgoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
