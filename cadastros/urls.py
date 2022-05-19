from django.urls import path

from . import views


app_name = 'paginas'
urlpatterns = [
    path('', views.CampoList.as_view(), name='index-cadastros'),
    path('campo/', views.CampoCreate.as_view(), name='cadastrar-campo'),
    path('atividade/', views.AtividadeCreate.as_view(), name='cadastrar-atividade'),
    path('campo/<int:pk>/update', views.CampoUpdate.as_view(), name='atualizar-campo'),
    path('atividade/<int:pk>/update', views.AtividadeUpdate.as_view(), name='atualizar-atividade'),
    path('campo/<int:pk>/delet', views.CampoDelete.as_view(), name='delet-campo'),
    path('atividade/<int:pk>/delet', views.AtividadeDelete.as_view(), name='delet-atividade'),
    path('atividades/', views.AtividadeList.as_view(), name='atividades'),
    
]