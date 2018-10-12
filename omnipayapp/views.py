from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Adding Comments

# Adding Comments

def hello(request):
   text = """<h2>Welcome to Omnipayapp+new_new port and I am runningashdbjhasjhdbajkdbjkhbv </h2>"""
   return HttpResponse(text)
