from django.shortcuts import render
from .models import Post

def get_ctfs():
    return [p.catagory for p in Post.objects.all()[::-1]][:5]

def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all(), 'ctfs': get_ctfs()})

def filter_for_ctf(request, ctf):
    return render(request, 'index.html', {'posts': Post.objects.filter(catagory__iexact=ctf), 'ctfs': get_ctfs()})

def get_post(request, ctf, pk):
    return render(request, 'post.html', {'p': Post.objects.get(pk=pk), 'ctfs': get_ctfs()})