from django.forms import ModelForm
from django import forms
from loveapp.models import Users

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    nome_loja = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nome da loja'}))
    cnpj = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CNPJ'}))
    class Meta:
        model = Users
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['usuario', 'senha', 'email', 'nome_loja', 'cnpj']