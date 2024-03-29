from django.shortcuts import render
from django.http import Http404
from blog.data import posts

# Create your views here.

def blog(request):
    print('Blog app 2!')
    return render(
        request,
        'blog/index.html',
        {
            'title': 'Blog',
            'posts': posts,
        }
    )
    
def post(request, post_id):
    
    found_post = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não encontrado')
    
    return render(
        request,
        'blog/post.html',
        {
            'title': 'post',
            'post': found_post
        }
    )

def exemplo(request):
    print('Exemplo app 2!')
    context = {
        'title': '- Exemplo',
        'text': 'Estamos na Exemplo'
    }
    return render(
        request,
        'blog/exemplo.html',
        context
    )
