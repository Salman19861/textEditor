from django.http import HttpResponse
from django.shortcuts import render
from typing import DefaultDict
def index(request):
    return render(request,"index.html")