from django.shortcuts import render
from main import models

# Create your views here.
def index(request):
    about_site = 'К блогам'
    news = models.News.objects.all()


    return render(request, 'index.html',
    {'about_site':about_site,
     'news':news})

def blogs(request):
    blogs = models.Blog.objects.all()
    return render(request, 'blogs.html',
    {'blogs':blogs})

def blog(request,blog_id):
    blog = models.Blog.objects.get(id=blog_id)
    return render(request, 'blog.html', {'blog':blog})
