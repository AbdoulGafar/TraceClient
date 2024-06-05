from django import forms
from .models import ClientInfo

class ClientInfoForm(forms.ModelForm):
    class Meta:
        model = ClientInfo
        fields = ['client_id', 'latitude', 'longitude', 'fingerprint']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'fingerprint': forms.HiddenInput(),
        }

