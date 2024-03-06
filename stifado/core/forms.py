from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# class CreateUserForm(UserCreationForm):
#     email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Email Address'}))
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']
#         def __init__(self,*args, **kwargs):
#             super(CreateUserForm,self).__init__(*args,**kwargs)

#             self.fields['username'].widget.attrs['class'] = ''