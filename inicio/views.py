from django.shortcuts import render

from django.http import HttpResponse

def saudacao(request, nome):
    return HttpResponse(f"Olá, {nome}!")
