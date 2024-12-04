from django import forms

from .models import Smartphone

class SmartphoneForm(forms.ModelForm):
    model = Smartphone
    fields= '__all__'
    
    def clean_price(self):
        price = self.cleaned_data['price']
        
        if price < 100:
            raise forms.ValidationError('El precio debe ser mayor a 100')
        
        return price