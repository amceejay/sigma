from operator import imod
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     return HttpResponse('Analyse your data on the fly')
