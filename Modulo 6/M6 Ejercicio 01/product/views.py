from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list(request):
    return render(request, 'product/list.html')

def add(request):
    return render(request,'product/add.html')

def edit(request):
    return render(request,'product/edit.html')