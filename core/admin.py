from django.contrib import admin
from .models import Inicio, Nosotros, Programas, Actividades, Historias, Articulos, Donaciones, DonacionesCBU, InicioSubPuntos, ImagenAnimada
from .models import NosotrosSubPuntos, NosotrosQueBuscamos

# Register your models here.
class ImagenAnimadaInline(admin.TabularInline):
    model = ImagenAnimada
    extra = 1  # Número de formularios vacíos adicionales
    readonly_fields = ('orden',)

class SubPuntoInLine(admin.TabularInline):
    model = InicioSubPuntos
    extra = 1
    readonly_fields = ('orden',)

class InicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'fecha_publicacion', 'fecha_modificacion')
    inlines = [SubPuntoInLine,ImagenAnimadaInline]
    list_filter = ('publicado', 'fecha_publicacion')
    search_fields = ('titulo',)

class NosotrosSubPuntoInLine(admin.TabularInline):
    model = NosotrosSubPuntos
    extra = 1
    readonly_fields = ('orden',)

class NosotrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado',)
    inlines = [NosotrosSubPuntoInLine]
    search_fields = ('titulo', 'contenido', 'mision')
    
class NosotrosBusquedaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado',)
    search_fields = ('titulo', 'imagen', 'video')
    

class ProgramasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado',)
    search_fields = ('titulo', 'contenido', 'info')

class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado',)
    search_fields = ('titulo', 'descripcion', 'info')

class HistoriasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado',)
    search_fields = ('titulo', 'testimonios')

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado',)
    search_fields = ('titulo', 'articulos')

class DonacionesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado',)
    search_fields = ('titulo', 'info', 'info_impacto')

class DonacionesCBUAdmin(admin.ModelAdmin):
    list_display = ('banco', 'publicado',)
    search_fields = ('banco','cbu','alias')

#class MyAdminSite(admin.AdminSite):
#    site_header = "Administración de la Fundación"
#    site_title = "FUTURAR"
#    index_title = "Administración de la Fundación"

#admin_site = MyAdminSite(name="myadmin")

admin.site.register(Inicio, InicioAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(NosotrosQueBuscamos, NosotrosBusquedaAdmin)
admin.site.register(Programas, ProgramasAdmin)
admin.site.register(Actividades, ActividadesAdmin)
admin.site.register(Historias, HistoriasAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Donaciones, DonacionesAdmin)
admin.site.register(DonacionesCBU, DonacionesCBUAdmin)