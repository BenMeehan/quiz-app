from django.urls import path
from qa import views

urlpatterns = [
    path('', views.index, name="index"),
    path('initial/', views.initial, name="index"),
    path('get_users_py/', views.get_users_py, name="index"),
    path('get_users_cn/', views.get_users_cn, name="index"),
    path('python/', views.python, name='python'),
    path('cn/', views.networks, name='python'),
    path('submit_python/', views.submit_python, name='python'),
    path('submit_networks/', views.submit_networks, name='python'),
]
