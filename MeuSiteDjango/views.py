from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
    return HttpResponse(_vira_html('Vá para <a href="loja">loja</a> ou <a href="vendas">vendas</a>'))

def _vira_html(mensagem : str):
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body> 
        <h1>WELLCOME TO THE DJUNGLE!!!</h1> 
        <p>{mensagem}</p>
    </body>
    </html>
    '''

def Logar(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html',{"erro": "Login falhou"})
    else:
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect("index")