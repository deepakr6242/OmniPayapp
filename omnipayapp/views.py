from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Adding Comments

def hello(request):
   text = """<h2>Welcome to Omnipayapp!</h2>"""
   return HttpResponse(text)