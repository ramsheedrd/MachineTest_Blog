from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify

from .models import PostModel, CATEGORY_CHOICES
from .forms import PostForm
from taggit.models import Tag

def home_view(request):
    return render(request, 'home.html')

def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.slug = slugify(newpost.heading)
            newpost.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
            return redirect('posts')
        else:
            return render(request, 'post_create.html', {'form':form})
    else:
        return render(request, 'post_create.html', {'form':PostForm()})

def post_list_view(request, category=None):
    if category:
        posts = PostModel.objects.filter(category=category).order_by('-published')
    else:
        posts = PostModel.objects.order_by('-published')
    context = {
        'posts':posts,
        'categories': CATEGORY_CHOICES,
    }
    return render(request, 'posts_list.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = PostModel.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'post_list.html', context)