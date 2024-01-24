from django.urls import path
from blog import views

# http://127.0.0.1:8000/blog/exemplo

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]