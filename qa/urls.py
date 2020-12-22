from django.urls import path
from qa import views

urlpatterns = [
    path('', views.index, name="index"),
    path('initial/', views.initial, name="initial"),
    path('get_users_py/', views.get_users_py, name="userspy"),
    path('get_users_cn/', views.get_users_cn, name="userscn"),
    path('get_users_java/', views.get_users_java, name="usersjava"),
    path('python/', views.python, name='python'),
    path('cn/', views.networks, name='networks'),
    path('java/', views.java, name='java'),
    path('submit_python/', views.submit_python, name='subpython'),
    path('submit_networks/', views.submit_networks, name='subnetworks'),
    path('submit_java/', views.submit_java, name='subjava'),
]
