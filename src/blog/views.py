from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from blog.models import BlogPost
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template.defaultfilters import slugify, striptags


def home(request):
    return HttpResponse("BIENVENUE !")

#@user_passes_test(lambda user: user.username == "test")
def blog_index(request):
    # Très interessant pour faire de l'API
    # return JsonResponse({"1": "Premier article du blog"})
    #return redirect("home") # Redirection vers la page "home" ou urls : "https://www.google.com"   
    # blog_post = get_object_or_404(BlogPost, pk=3) # On récupère l'objet sinon erreur 404
    posts = BlogPost.objects.filter(pk__in = [2,3,4,5])

    return render(request, "blog/index.html", context={
        "posts": posts})

def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)

    post_slug = slugify(post.title)

    response = render(request, "blog/post.html", {
        "post": post,
        "post_slug": post_slug}) 
    
    return response