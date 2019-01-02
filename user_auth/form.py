from django import forms

class AuthForm(forms.Form):
    login = forms.CharField(max_length=255,
        widget=forms.TextInput(
            attrs={'id': 'inputEmail', 'class': 'form-control', 'placeholder':"Логин"}), label='логин')
    password = forms.CharField(max_length=255,
        widget=forms.PasswordInput(
            attrs={'id': 'inputPassword', 'class': 'form-control', 'placeholder':"Пароль"}))
