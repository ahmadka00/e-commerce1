from django import forms
from .models import UserBase
from django.contrib.auth import forms as form


# class RegistrationForm(forms.ModelForm):

#     user_name = forms.CharField(
#         label= 'Enter Username', min_length=4, max_length=50, help_text='Required')
#     email = forms.EmailField(max_length=100, help_text='Required', error_messages={
#         'required': 'Sorry, you will need an email'})
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

#     class Meta:
#         model = UserBase
#         fields = ('user_name', 'email',)



class RegistrationForm(form.UserCreationForm):
    class Meta:
        model = UserBase
        fields = ['user_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].widget = forms.TextInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Username',
            'autocomplete': 'off',
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Email Address',
            'autocomplete': 'off',
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingPassword',
            'placeholder': 'Password',
            'autocomplete': 'off',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingPassword',
            'placeholder': 'Confirm Password',
            'autocomplete': 'off',
        })



class UserEditForm(form.UserChangeForm):

    class Meta:
        model = UserBase
        fields = ['user_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].widget = forms.TextInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Username',
            'autocomplete': 'off',
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Email Address',
            'autocomplete': 'off',
        })



# password Reset Form

class UserPasswordChangeForm(form.PasswordChangeForm):

    model = UserBase
    fields = ['old_password', 'new_password1', 'new_password2']
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingOldPassword',
            'placeholder': 'Old Password',
            'autocomplete': 'off',
        })
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword1',
            'placeholder': 'New Password',
            'autocomplete': 'off',
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword2',
            'placeholder': 'Confirm New Password',
            'autocomplete': 'off',
        })


class UserPasswordResetForm(form.PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingInput',
            'placeholder': 'Email Address',
            'autocomplete': 'off',
        })


class UserPasswordResetConfirmViewForm(form.SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword1',
            'placeholder': 'New Password',
            'autocomplete': 'off',
        })
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control rounded-3',
            'id': 'floatingNewPassword2',
            'placeholder': 'Confirm New Password',
            'autocomplete': 'off',
        })