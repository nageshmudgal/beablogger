from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def bloghome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog/bloghome.html", context)

def blogpost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    #OR post=Post.objects.filter(slug=slug)[0]
    comments = BlogComment.objects.filter(post=post)
    context={'post':post, 'comments': comments, 'user': request.user}
    return render(request, "blog/blogpost.html", context)
    #return HttpResponse(f"this is blogpost: {slug}")     #f is f string


def postComment(request):
    if request.method == "POST":
        comm = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        comment = BlogComment(comment=comm, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/blog/{post.slug}")
