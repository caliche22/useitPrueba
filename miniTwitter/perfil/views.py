from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template



def Principal(request): ## primera vista 
    doc_externo=open("C:/Users/calic/Desktop/MiniTwitter/Templates/template.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    documento=plt.render
    return HttpResponse(documento)



# Create your views here.
