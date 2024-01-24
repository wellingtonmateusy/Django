from django.shortcuts import render
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
    
    return render(
        request,
        'blog/index.html',
        {
            'title': 'Post',
            'posts': found_post,
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
        context,
    )
