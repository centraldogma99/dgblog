import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, SignupForm, CommentForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form':form})

    
@login_required
def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form':form,'title':post.title})
    
    
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull = True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts':posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    messages.info(request, 'Publish successful!')
    return redirect('post_detail', pk=pk)


@login_required
def post_unpublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.unpublish()
    messages.info(request, 'Unpublish successful!')
    return redirect('post_detail', pk=pk)


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect("post_list")


@require_POST
def post_like(request):
    pk = request.POST.get('pk',None)
    post = get_object_or_404(Post, pk=pk)
    post.post_like()
    message = "successful"
    context = {'like_count': post.likes,
               'message': message }
    return HttpResponse(json.dumps(context), content_type="application/json")
    

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password')
            #user = User.objects.create_user(username=username, password=raw_password)
        return redirect("post_list")
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form':form})


def comment_write2(request, pk, parent=None):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            if parent:
                com.parent = Comment.objects.get(pk=parent)    # 이곳
            com.post = get_object_or_404(Post, pk=pk)
            com.save()
            return redirect("post_detail", pk=pk)


def comment_remove(request, commentpk):
    comm = get_object_or_404(Comment, pk=commentpk)
    comm.delete()
    return redirect('post_detail', pk=comm.post.pk)


def comment_approve(request, commentpk):
    comm = get_object_or_404(Comment, pk=commentpk)
    comm.approve()
    comm.save()
    return redirect('post_detail', pk=comm.post.pk)
