from django import forms
from .models import Item
from django.core.exceptions import ValidationError

class ItemForm(forms.ModelForm):
    new_category = forms.CharField(
        required=False,
        label="Neue Kategorie",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Neue Kategorie eingeben'})
    )

    class Meta:
        model = Item
        fields = ['name', 'quantity', 'description', 'category'] 

    def clean_name(self):
        name = self.cleaned_data.get('name')
        owner = self.instance.owner if self.instance and self.instance.pk else self.initial.get('owner')
        
        if not name or name.strip() == '':
            raise ValidationError("Name darf nicht leer sein.")
        
        
        if Item.objects.filter(owner=owner, name__iexact=name).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Du hast bereits ein Item mit diesem Namen.")
        
        return name


    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Menge darf nicht negativ sein.")
        return quantity
