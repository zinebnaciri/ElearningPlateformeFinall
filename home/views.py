from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import NewsAndEventsForm
from .models import *

User = settings.AUTH_USER_MODEL

@login_required
def home_view(request):
    items = NewsAndEvents.objects.all().order_by('-updated_date')
    context = {
        'title': "News & Events ",
        'items': items,
    }
    return render(request, 'home/index.html', context)


@login_required
def post_add(request):
    if request.method == 'POST':
        form = NewsAndEventsForm(request.POST)
        title = request.POST.get('title')
        if form.is_valid():
            form.save()

            messages.success(request, (title + ' has been uploaded.'))
            return redirect('acceuil')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = NewsAndEventsForm()
    return render(request, 'home/ajout_post.html', {
        'title': 'Add Post ',
        'form': form,
    })


@login_required
def edit_post(request, pk):
    instance = get_object_or_404(NewsAndEvents, pk=pk)
    if request.method == 'POST':
        form = NewsAndEventsForm(request.POST, instance=instance)
        title = request.POST.get('title')
        if form.is_valid():
            form.save()

            messages.success(request, (title + ' has been updated.'))
            return redirect('acceuil')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = NewsAndEventsForm(instance=instance)
    return render(request, 'home/ajout_post.html', {
        'title': 'Edit Post   ',
        'form': form,
    })


@login_required
def delete_post(request, pk):
    post = get_object_or_404(NewsAndEvents, pk=pk)
    title = post.title
    post.delete()
    messages.success(request, (title + ' has been deleted.'))
    return redirect('acceuil')
