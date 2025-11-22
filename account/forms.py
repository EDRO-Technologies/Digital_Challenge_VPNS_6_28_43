from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={"class" : "email__input", "placeholeder" : "Электронная почта"}
        ),
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={"class" : "password__input", "placeholder" : "Пароль"} 
        ),
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