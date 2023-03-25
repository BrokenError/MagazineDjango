from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 25)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, empty_value=1, label='Кол-во')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

