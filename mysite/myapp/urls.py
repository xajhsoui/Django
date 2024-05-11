from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('home', views.home, name='home'),  # 追加する
    path('index', views.index, name='index')  # 追加する
]