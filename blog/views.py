from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Prashant Kalyani',
        'title' : 'Blog Post 1',
        'content' : 'First post',
        'date' : 'December 22, 2021'
    },
    {
        'author':'Shradha Kalyani',
        'title' : 'Blog Post 2',
        'content' : 'Second post',
        'date' : 'December 22, 2021'
    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')