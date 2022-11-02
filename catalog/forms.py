from django import forms
  
# creating a form
class InputForm(forms.Form):
  
    catet_1 = forms.CharField(max_length = 200)
    catet_2 = forms.CharField(max_length = 200)