from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from loveapp.models import Usuario, Comentario
from loveapp.forms import UsersForm, comentarioForm

# Create your views here.

def home(request):
    profile = {}
    try:
        profile['perfil'] = Usuario.objects.get(id=request.session['uid'])
        profile['custom'] = "Sair"    #quando estiver logado aparece logout
    except KeyError:
        profile['custom'] = "Logar"     #quando nao estiver logado aparece login
    print(profile['custom'])
    return render(request,'home.html',profile)

""" def home(request):
    profile = {}
    profile['uid'] = request.session['uid']
    return render(request,'home.html',profile) """



def cadastro(request):
    data = {}
    data['form'] = UsersForm()
    return render(request,'cadastro.html',data)

def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    for c in tabela:
        if form['usuario'].data == c.usuario:
            return render(request, 'errouser.html')
        if form['email'].data == c.email:
            return render(request, 'erromail.html')
        if form['cnpj'].data == c.cnpj:
            return render(request, 'errocnpj.html')
    if form.is_valid():
        form.save()
        return render(request, 'sucessocad.html')
    else:
        #return HttpResponse(form.errors)
        return render(request, 'errocad.html')


def sucessocad(request):
    return render(request, 'sucessocad.html',)

def errouser(request):
    return render(request, 'errouser.html',)

def erromail(request):
    return render(request, 'erromail.html',)

def errocnpj(request):
    return render(request, 'errocnpj.html',)

def errocad(request):
    return render(request, 'errocad.html',)


def login(request):
    data = {}
    data['form'] = UsersForm()
    return render(request, 'login.html',data)

def dologin(request):
    if request.method == "POST":
        tabela = Usuario.objects.all()
        form = UsersForm(request.POST or None)
        try:
            u = Usuario.objects.get(usuario=request.POST['usuario'])
        except:
            return HttpResponse("Falha no login")
        if u.senha == request.POST['senha']:
            request.session['uid'] = u.id
            return redirect('home')
        else:
            return HttpResponse("Falha no login")
    else:
        redirect('login')

def dologout(request):
    if request.session['uid'] != "" or request.session['uid'] != None:
        try:
            del request.session['uid']  #apaga a sessão
            return render(request, 'logout.html')     #depois colocar redirect bunitin
        except KeyError:
            return redirect('home')
    return redirect('home')

def profile(request):
    profile = {}
    try:
        profile['perfil'] = UsersForm(instance=Usuario.objects.get(id=request.session['uid']))
        return render(request,'editprofile.html', profile)
    except KeyError:
        return HttpResponse('vc ñ esta logado')

def doupdate(request):
    form = {}
    form['user'] = Usuario.objects.get(id=request.session['uid'])
    form['user'].usuario = request.POST['usuario']
    form['user'].email = request.POST['email']
    form['user'].nomeloja = request.POST['nomeloja']
    form['user'].cnpj = request.POST['cnpj']
    form['user'].save()
    return redirect('home')


def comentario(request):
    data = {}
    if request.method == 'POST':
        c = Comentario(usuario=Usuario.objects.get(id=request.session['uid']),comentario=request.POST['comentario'])     
        c.save()
        return redirect ('comentario')
    else:
        data['form'] = comentarioForm()
        data['history'] = Comentario.objects.filter(usuario=request.session['uid'])
        print(data['history'])
        return render(request,'comentario.html',data)

def edit_coment(request, id):
    c = Comentario.objects.get(id=id)
    if request.method == 'POST':
        f = comentarioForm(request.POST,instance=c)
        f.save()
        return redirect ('comentario')
    else:
        f = comentarioForm(instance=c)
        return render(request, 'comentario.html',{'form':f})