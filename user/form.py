from django import forms


class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı ")
    password=forms.CharField(label="Parola ",widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username=forms.CharField(min_length=10,max_length=50,label="Kullanıcı Girişi ")
    password=forms.CharField(max_length=50,label="Parola ",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=50,label="Parola Doğrula ",widget=forms.PasswordInput)
    
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password !=confirm:
            raise forms.ValidationError("Parolalar Eşleşmedi...")

        values= {
            "username" : username,
            "password" : password
        }
        return values

