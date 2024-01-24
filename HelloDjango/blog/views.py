from django.shortcuts import render

# Create your views here.

def blog(request):
    print('Blog app 2!')
    context = {
        'title': '- Blog',
        'text': 'Estamos na Blog'
    }
    return render(
        request,
        'blog/index.html',
        context,
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
