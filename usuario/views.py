from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def cadastro (request):
    if request.method =='GET':
        return render (request,'cadastro.html')
    else:
        username=request.POST.get('username')
        email=request.POST.get('email')
        senha=request.POST.get('senha')
        user =User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse usernme')
        
        user=User.objects.create_user(username=username,password=senha, email=email)
        user.save()
        return HttpResponse('usuario cadastrado com sucesso')

def login (request):
    if request.method=='GET':
        return render (request,'login.html')
    else:
        username=request.POST.get('username')
        senha=request.POST.get('senha')
        user=authenticate(username=username, password=senha)
        if user:
            return HttpResponse('autenticado')
        else:
            return HttpResponse('email ou usurio invalido')
            
