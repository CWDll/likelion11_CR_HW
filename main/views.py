from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blog/detail.html', {'blog': blog})

def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'main/detail.html', {'blog':blog})

def mainpage(request):
    blogs = Blog.objects.all()
<<<<<<< HEAD
    return render(request, 'main/mainpage.html', {'blogs':blogs})
=======
    return render(request, 'main/mainpage.html', {'blogs': blogs})
>>>>>>> 7c46afe8e19fddf1c5d717d94f9e66669aca341f

def secondpage(request):
    return render(request, 'main/secondpage.html')

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
<<<<<<< HEAD
    
    new_blog.save()

    return redirect('detail', new_blog.id)
    
=======

    new_blog.save()

    return redirect('detail', new_blog.id)

>>>>>>> 7c46afe8e19fddf1c5d717d94f9e66669aca341f
def new(request):
    return render(request, 'main/new.html')