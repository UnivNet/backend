from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def login(request):
    text = """<h1>Welcome Page </h1><h2>Work still in progess</h2>"""
    return HttpResponse(text)
