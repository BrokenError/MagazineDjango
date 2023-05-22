from django import forms


class OrderCreateForm(forms.Form):
    description = forms.CharField(label='Комментарий')
    deliv_address = forms.CharField(label='Адрес доставки')
    paid = forms.BooleanField(label='Оплачено')
