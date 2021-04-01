from django import forms
from django.contrib.auth import get_user_model

# Check for unique username and password

User = get_user_model()

not_allowed_username = ['abc','pqr']

# Register forms
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-confirm-password'
            }
        )
    )
    def clean_username(self):       #clean each username
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username) #thisIsMyUsername == thisismyusername
        if username in not_allowed_username:
            raise forms.ValidationError("This is a not allowed Username. Pick another one.")
        if qs.exists():
            raise forms.ValidationError("This is an Invalid Username. Pick another one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email


# standard form different from modelForm as in product/forms.py
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )

    # def clean(self):        # in future clean for additional features user and passwords
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')


    def clean_username(self):       #clean each username
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username) #thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an Invalid User.")
        return username
    
