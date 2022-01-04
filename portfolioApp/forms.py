from django import forms
from .models import *


#
class contactForm(forms.ModelForm):
	class Meta:
		model = lead_contacts
		exclude = ('publish','created','updated','status')
