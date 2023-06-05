from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from app.forms import *
# Create your views here.
def list_view(request):
    context = {
        "blogs" : Blog.objects.all(),
    }
    return render(request, 'pages/list.html', context)
def details_view(request,id):
    context = {
        "blog" : Blog.objects.get(id=id)
    }
    return render(request, 'pages/details.html', context)
def create_view(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        'form': form,
    }   
    return render(request, 'pages/create.html', context)
def update_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST , instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "form": form,
    }
    return render(request, 'pages/update.html', context)
def delete_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('list')