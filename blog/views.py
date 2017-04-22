from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
import datetime


def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    #variables to @media image
    pagetitle = "Blog"
    subtitle = "New ideas for your events"
    # now return the rendered template
    return render(request, 'blog_index.html', {'posts': Post.objects.all(), 'pagetitle':pagetitle, 'subtitle':subtitle})

def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})

def post_detail(request, id):
    """
    Create a view that return a single
    Post object based on the post ID and
    and render it to the 'postdetail.html'
    template. Or return a 404 error if the
    post is not found
    """
    post = get_object_or_404(Post, pk=id)
    pagetitle = post.title
    return render(request, "postdetail.html", {'post': post, 'pagetitle':pagetitle})


#@login_required(login_url='/login/')
def new_post(request):
    if request.method =="POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blogpostform.html',{'form': form})

def edit_post(request,id):
    post=get_object_or_404(Post, pk=id)
    if request.method =="POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/blogpostform.html',{'form': form})