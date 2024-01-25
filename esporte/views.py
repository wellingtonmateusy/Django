from django.shortcuts import render
from django.http import Http404
from esporte.data import posts

# Create your views here.

def esporte(request):
    print('Esporte!')
    return render(
        request,
        'esporte/index.html',
        {
            'title': 'Esporte',
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
        raise Http404('Post não encontrado!')
    
    return render(
        request,
        'esporte/post.html',
        {
            'title': 'post',
            'post': found_post
        }
    )
