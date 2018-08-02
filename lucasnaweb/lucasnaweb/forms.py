from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensagem = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))