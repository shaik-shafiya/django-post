from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.

def index(request):

    abc = Post.objects.all()

    print(abc)

    return render(request, 'index.html',context={'abc':abc})

def about(request):
    return render(request,'about.html')
