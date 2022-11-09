from django import forms


class triangle_form(forms.Form):
    leg_1 = forms.FloatField(label='Leg 1', min_value=1, required=True)
    leg_2 = forms.FloatField(label='Leg 2', min_value=1, required=True)
