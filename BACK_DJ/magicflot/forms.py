from django import forms
from .models import Winner

class WinnerForm(forms.ModelForm):
	class Meta:
		model = Winner
		fields = ['first_name', 'last_name', 'school', 'the_class']