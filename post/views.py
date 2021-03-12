from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView
)
from post.models import (
    Like, Post
)
from post.forms import PostForm


class BlogListView(ListView):
    template_name = "post/home.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:5]


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit.html', {'form': form})


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    qs = Like.objects.filter(user=request.user, post=post)
    if qs.exists():
        qs[0].delete()
    else:
        Like.objects.create(user=request.user, post=post)
    return redirect("/")
