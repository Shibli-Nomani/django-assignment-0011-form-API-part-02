#import form API
from django import forms 
#example:validating the email digits
from django.core import validators


class AgentProfile(forms.Form):
    first_name = forms.CharField(max_length= 50, required=False)
    last_name = forms.CharField(label = "Last Name", max_length=50)
    email = forms.EmailField(label="Enter Your Email", validators= [validators.MaxLengthValidator(30)])
    acode = forms.IntegerField(help_text= "Must Be Filled", min_value= 1)
    mobile = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=15)
    #example: field-matching: password matching pass/re-pass
    
    re_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=15)
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows' : 5, 'cols' : 30}))
    checkbox = forms.CharField(widget=forms.CheckboxInput())
    registration_fee = forms.DecimalField(min_value= 2500, max_digits= 6, decimal_places= 2 )
    agree = forms.BooleanField(label = "I agree with your terms")

    #to apply password matching condition
    #self is an instance to access the method and attributes
    #create clean method
    #super() function is used to give access to methods and properties of a parent or sibling class.
    #and return the object of parents class
    def clean(self):
        cleaned_data =super().clean
        pass_match = self.cleaned_data['password']
        re_pass_match = self.cleaned_data['re_password']

        if pass_match != re_pass_match:
            raise forms.ValidationError("password not match")
    

