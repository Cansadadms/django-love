from django.forms import ModelForm
from django import forms
from loveapp.models import Usuario, Comentario

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'maxlength':'16'
        }))
    usuario = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Usuário',
        'maxlength':'16'
        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'maxlength':'45'
        }))
    nomeloja = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nome da loja',
        'onkeypress': 'regex_nomeloja(event)',
        'maxlength':'45'
        }))
    cnpj = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'CNPJ', 
        'onkeypress': 'regex_cnpj(event)',
        'maxlength':'14'
        }))

    class Meta:
        model = Usuario 
        fields = ['usuario', 'senha', 'email', 'nomeloja', 'cnpj']


class comentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario']