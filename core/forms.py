from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'id': 'contact-name',
            'data-constraints': '@Required'
        })
        )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class':'form-input',
            'id':'contact-email',
            'data-constraints': '@Email @Required'
        })
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input',
            'id': 'contact-message',
            'data-constraints': '@Required'
        })
        )

class DonacionForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo_electronico = forms.EmailField()
    #cantidad = forms.DecimalField(max_digits=10, decimal_places=2)
    #metodo_pago = forms.ChoiceField(choices=[('Mercado Pago', 'Mercado Pago'), ('tarjeta', 'Tarjeta de Crédito','Tarjeta de Débito')])
    mensaje = forms.CharField(widget=forms.Textarea, required=False)
