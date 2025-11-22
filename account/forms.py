from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={"type": "email", "id":"email", "name":"email", "placeholder":"Почта"}
        ),
        label="Почта"
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={"class": "password__input", "type": "password", "id": "password", "name": "password", "placeholder" :"Пароль"} 
        ),
        label="Пароль"
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise ValidationError("Неправильная почта или пароль.")
            self.user = user

        return cleaned_data

    def get_user(self):
        return getattr(self, 'user', None)