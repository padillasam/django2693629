from django.urls import path
from . import views
urlpatterns = [
    path('lista/',views.usuariolist,name="usuario_list"),
    path('indexFormulario/',views.indexFormulario,name="index_formulario"),
    path('procesarFormulario/',views.procesarFormulario,name="procesar_formulario"),

]
