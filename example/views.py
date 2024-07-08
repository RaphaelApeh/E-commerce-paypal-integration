from django.shortcuts import render
from django.http import JsonResponse

from .models import Example

def home(request):
    return render(request,'example/index.html',{})

def example(request):
    example = Example.objects.all()
    return JsonResponse({'model':list(example.values())})