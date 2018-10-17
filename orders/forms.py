from django.forms import ModelForm
from django import forms
from .models import Order

class OrderForm(ModelForm):
    OPTIONS = (
        (0,'À vista - dinheiro'),
        (1,'Débito'),
        (2,'Crédito'),
    )
    # OPTIONS2 = (
    #     (0, 'Confirmado'),
    #     (1, 'Pronto'),
    #     (2, 'Enviado'),
    #     (3, 'Entregue'),
    #     (4, 'Retornado'),
    #     (5, 'Cancelado')
    # )
    #order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','amount','order_status']