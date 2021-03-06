from django import forms
from .models import Feed
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
#        practiceArea = forms.ChoiceField(choices=CATEGORIES)
        fields = ('url','practiceArea', 'author')


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("This user does not exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")
        if not user.is_active:
            raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm,self).clean(*args,**kwargs)
