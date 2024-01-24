from django.shortcuts import render

# Create your views here.

def home(request):
    print('Home 5!')
    context = {
        'title': '- Home',
        'text': 'Estamos na Home'
    }
    return render(
        request,
        'home/index.html',
        context,
    )