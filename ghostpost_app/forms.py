from django import forms
from ghostpost_app.models import BR_Post


class BR_PostForm(forms.Form):
    title = forms.CharField(max_length=280)
    boast_roast = forms.BooleanField()
    up_field = forms.IntegerField()
    down_field = forms.IntegerField()
