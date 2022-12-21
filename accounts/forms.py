from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class AddUserForm(forms.ModelForm):

    password1 = forms.CharField()
    password2 = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser' )

    def clean_password2(self):
        
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            
            raise forms.ValidationError("Passwords didn't match. Try again.")
        
        return self.cleaned_data


    def save(self, commit=True):
        
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user