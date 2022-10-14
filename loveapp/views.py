from django.shortcuts import render, redirect
from loveapp.models import Users
from loveapp.forms import UsersForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)

def docad(request):
	tabela = Users.objects.all()
	form = UsersForm(request.POST or None)
	for c in tabela:
		if form['usuario'].data == c.usuario:
			return render(request, 'errocad.html')
	if form.is_valid():
		form.save()
	return render(request, 'sucessocad.html')

def errocad(request):
    return render(request, 'errocad.html',)

def sucessocad(request):
    return render(request, 'sucessocad.html',)

def login(request):
    tabela = Users.objects.all()
    return render(request,'login.html',{'usuario':tabela})