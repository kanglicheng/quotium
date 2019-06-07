from django import forms
from .models import PropertyData
from django.utils.translation import gettext_lazy as _


class SubmissionForm(forms.ModelForm):

    class Meta:
        model = PropertyData
        fields = ('email', 'property_address', 'zip_code', 'number_bedrooms', 'number_bathrooms', 'square_footage')

        labels = {
            'property_address': _('Property Address'),
            'zip_code': _('Zip Code'),
            'number_bedrooms': _('Number of Bedrooms'),
            'number_bathrooms': _('Number of Bathrooms'),
            'square_footage': _('Square Footage'),
        }
        widgets = {
            'number_bathrooms': forms.NumberInput(attrs={'step':0.5}),
        }
