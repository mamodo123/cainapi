from django.http import HttpResponse
from django.shortcuts import render

def loveyou(request):
    return render(request, "iloveyou.html")