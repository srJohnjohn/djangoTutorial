from django.urls import path

from . import views


app_name = 'paginas'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='paginas-index'),
]