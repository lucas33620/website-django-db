from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from blog.models import BlogPost
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    return HttpResponse("BIENVENUE !")

@user_passes_test(lambda user: user.username == "test")
def blog_posts(request):
    # Très interessant pour faire de l'API
    # return JsonResponse({"1": "Premier article du blog"})
    #return redirect("home") # Redirection vers la page "home" ou urls : "https://www.google.com"   
    blog_post = get_object_or_404(BlogPost, pk=3)

    return HttpResponse(blog_post.content)

def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    response = render(request, "blog/post.html", {"blog_post": post}) 
    return response