from django import forms
from django.contrib.auth import (authenticate, get_user_model,User)



class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    def limpiar(self, *args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            usuario=authenticate(username=username,password=password)
            if not usuario:
                raise forms.ValidationError('Este usuario no existe')
            if not usuario check_password(password):
                raise forms.ValidationError('Contraseña incorrecta')
        return super(UserLoginForm,self).limpiar(*args, **kwargs)


class UserRegisterForm():
    email=forms.EmailField(label='Email')
    emailconfirm=forms.EmailField(label='Confirmacion Email')

    class Meta:
        model=User
        campos=['username','email','emailconfirm','password']

    def limpiar2(self):
        email=self.cleaned_data.get('email')
        emailconfirm=self.cleaned_data.get('emailconfirm')
        if  email !=emailconfirm:
            raise forms.ValidationError('los emails no son iguales')
        email_e=User.objects.filter(email=email)
        if email_e.exists():
            raise forms.ValidationError('el email ya existe')

        return email

