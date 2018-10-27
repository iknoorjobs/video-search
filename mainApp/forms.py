from django import forms


class VidOpenForm(forms.Form):
	url = forms.URLField()
	