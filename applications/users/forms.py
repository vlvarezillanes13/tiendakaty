from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'',
                'style':'{ margin: 10px }',
                'class':"form-control",
                'id':"floatingInput",
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'',
                'class':"form-control",
                 'id':"floatingPassword"
            }
        )
    )


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username_ = self.cleaned_data['username']
        password_ = self.cleaned_data['password']
        
        if not authenticate(username=username_, password=password_):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        
        return self.cleaned_data