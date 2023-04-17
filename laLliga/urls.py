from django.urls import path
from . import views,api

urlpatterns = [
    path('', views.index, name='index'),
    path('classificacio',views.classificacio),
    path('classificacio/<int:lliga_id>',views.classificacio, name="classificacio"),
    path('menu',views.menu),
    path('crearLliga',views.crearLliga, name="crearLliga"),
    path('crea_Partit',views.crearPartit, name="crearPartit"),
    path('crea_Partit/<int:lliga_id>',views.triarEquipsPartit, name="triarEquipsPartit"),
    path('api/get_lligues',api.getLligues, name="getLligues"),
    path('editar_partit',views.editarPartitAdvanced, name="editarPartitAdvanced"),
    path('api/get_equips/<int:lliga_id>',api.getEquips, name="getEquips"),
]