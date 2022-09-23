from django.shortcuts import render,redirect
from loveapp.models import Users
from loveapp.forms import UsersForm

# Create your views here.

def home (request):
    return render(request,'home.html',{})


def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def docad(request):
	tabela = Users.objects.all()
	form = UsersForm(request.POST or None)
	erro = ''
	for c in tabela:
		if form['usuario'].data == c.usuario:
			erro = 'Mensagem de erro'
	print(erro)
	if form.is_valid() and erro == '':
		form.save()
	return redirect('cadastro')

def teste (request):
	tabela = Users.objects.all()
	return render(request,'teste.html',{'usuario':tabela})

