from django.urls import path
from login import views

app_name = "login"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/add', views.add, name='add'),
    path('index/show', views.show, name='show'),
    path('index/modify/<order_id>/', views.modify, name='modify'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]