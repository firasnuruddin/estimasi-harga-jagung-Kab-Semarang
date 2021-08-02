from django import forms


class JagungForm(forms.Form):
    luas_tanah = forms.CharField(max_length=100)
    luas_area = forms.CharField(max_length=100)
    luas_bumi = forms.CharField(max_length=100)
