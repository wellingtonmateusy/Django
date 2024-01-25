from django.urls import path
from esporte import views

app_name = 'esporte'

urlpatterns = [
    path('', views.esporte, name = 'home'),
    path('post/<int:post_id>/', views.post, name= 'post'),
]