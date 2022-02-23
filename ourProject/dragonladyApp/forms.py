from dataclasses import field
from socket import fromshare
from django import forms

from .models import Registration

class RegistrationForm (forms.ModelForm):
    gender = [
        ('M','Male'),
        ('F','Female'),
        ('NB','Non-Binary'),
        ('T','Transgender'),
        ('I','Intersex'),
        ('IPNTS','I prefer not to say'),
    ]

    first_name = forms.CharField (required=True, widget=forms.TextInput(attrs={'class':'first__form-control', 'placeholder':'Enter your First Name'}))
    middle_name = forms.CharField (required=True, widget=forms.TextInput(attrs={'class':'first__form-control', 'placeholder':'Enter your Middle Name'}))
    surname = forms.CharField (required=True, widget=forms.TextInput(attrs={'class':'first__form-control', 'placeholder':'Enter your Surname'}))
    age = forms.IntegerField (required=True, widget=forms.NumberInput(attrs={'type':'number', 'class':'first__form-control', 'placeholder':'Enter Age'}))
    birthday = forms.DateField (required=True, widget=forms.widgets.DateInput(attrs={'type': 'date', 'class' : 'first__form-control'}))
    gender = forms.CharField (widget=forms.Select(choices=gender, attrs={'class' : 'first__form-control'}))
    email_address = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class' : 'first__form-control', 'placeholder': 'Enter your Email Address'}))
    home_address = forms.CharField (required=True, widget=forms.TextInput(attrs={'class':'first__form-control', 'placeholder':'Enter your Home Address'}))
    borrower_code = forms.CharField (required=True, widget=forms.TextInput(attrs={'class':'first__form-control'}))
    valid_id = forms.ImageField (required=True, widget=forms.FileInput(attrs={'type':'file', 'class':'first__form-control'}))

    class Meta:
        model = Registration
        fields = "__all__"

    def save(self):
        borrower = super().save
        borrower.first_name = self.cleaned_data.get('first_name')
        borrower.middle_name = self.cleaned_data.get('middle_name')
        borrower.surname = self.cleaned_data.get('surname')
        borrower.age = self.cleaned_data.get('age')
        borrower.birthday = self.cleaned_data.get('birthday')
        borrower.gender = self.cleaned_data.get('gender')
        borrower.email_address = self.cleaned_data.get('email_address')
        borrower.home_address = self.cleaned_data.get('home_address')
        borrower.borrower_code = self.cleaned_data.get('borrower_code')
        borrower.valid_id = self.cleaned_data.get('valid_id')
        borrower.save()

        return borrower
