from django.urls import path
from . import views
from django.contrib import admin
#from .admin import admin_site

urlpatterns = [
    #path('admin/',admin_site.urls),
    path('',views.inicio,name='inicio'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('programas/',views.programas,name='programas'),
    path('actividades/',views.actividades,name='actividades'),
    path('historias/',views.historias,name='historias'),
    path('actividad/<int:id>/',views.actividad_detalle, name='actividad_detalle'),
    #path('articulos/',views.articulos,name='articulos'),
    path('donaciones/',views.donaciones,name='donaciones'),
    path('contacto/',views.contacto,name='contacto'),
    # contacto y donación redirección:
    path('contacto/exito/', views.contacto_exito, name='contacto_exito'),
    path('contacto/fallo/', views.contacto_fallo, name='contacto_fallo'),
]