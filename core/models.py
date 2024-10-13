from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

# Create your models here.
class Inicio(models.Model):
    titulo = models.CharField(max_length=200)
    que_ofrecemos = RichTextField(null=True)
    mision = RichTextField(null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    video = models.URLField(blank=True, null=True)
    publicado = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Inicio"
        verbose_name_plural = "Inicio"

class ImagenAnimada(models.Model):
    inicio = models.ForeignKey(Inicio, related_name='imagenes_animadas', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='inicio/animated/')
    orden = models.PositiveIntegerField(default=0)  # Para mantener el orden de las imágenes

    def __str__(self):
        return f"Imagen {self.orden} de {self.inicio.titulo}"

    class Meta:
        ordering = ['orden']
        verbose_name = "Imagen Animada"
        verbose_name_plural = "Imágenes Animadas"

class InicioSubPuntos(models.Model):
    inicio = models.ForeignKey(Inicio, related_name='sub_puntos', on_delete=models.CASCADE)
    sub_punto_titulo = models.CharField(max_length=200,default="titulo")
    sub_punto_parrafo = RichTextField()
    orden = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.sub_punto_titulo
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Subpunto de Inicio"
        verbose_name_plural = "Subpuntos de Inicio"
        
class Nosotros(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='nosotros/', blank=True,null=True)
    video = models.URLField(blank=True, null=True)
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

    def get_embed_url(self):
        if self.video and 'youtube.com/watch' in self.video:
            video_id = self.video.split('v=')[-1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    class Meta:
        verbose_name = "Sobre Nosotras"
        verbose_name_plural = "Sobre Nosotras"
        
class NosotrosSubPuntos(models.Model):
    inicio = models.ForeignKey(Nosotros, related_name='sub_puntos', on_delete=models.CASCADE)
    sub_punto_titulo = models.CharField(max_length=200,default="titulo")
    sub_punto_parrafo = RichTextField()
    orden = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.sub_punto_titulo
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Subpunto de Nosotros"
        verbose_name_plural = "Subpuntos de Nosotros"        
        
class NosotrosQueBuscamos(models.Model):
    titulo = models.CharField(max_length=200)
    campo_texto = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='nosotros/', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

    def clean(self):
        # Contar cuántos campos tienen valor
        filled_fields = sum([bool(self.campo_texto), bool(self.imagen), bool(self.video)])

        # Asegurarse de que solo uno de los campos esté lleno
        if filled_fields > 1:
            raise ValidationError("Solo se puede completar uno de los siguientes campos: campo_texto, imagen o video.")
        if filled_fields == 0:
            raise ValidationError("Debes completar al menos uno de los siguientes campos: campo_texto, imagen o video.")

    def get_embed_url(self):
        if self.video and 'youtube.com/watch' in self.video:
            video_id = self.video.split('v=')[-1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    class Meta:
        verbose_name = "Que Buscamos"
        verbose_name_plural = "Que Buscamos Nosotras"

class Programas(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = RichTextField()
    info = RichTextField()
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"

class Actividades(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    info_detalle = RichTextField(null=True)
    horario = models.DateTimeField(null=True)
    imagen_actividad = models.ImageField(null=True)
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
  

class Historias(models.Model):
    titulo = models.CharField(max_length=200)
    testimonios = RichTextField()
    enlaces = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='historias/', blank=True,null=True)
    video = models.URLField(blank=True, null=True)
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

    def get_embed_url(self):
        if self.video and 'youtube.com/watch' in self.video:
            video_id = self.video.split('v=')[-1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None
    
    class Meta:
        verbose_name = "Historias"
        verbose_name_plural = "Historias"

class Articulos(models.Model):
    titulo = models.CharField(max_length=200)
    articulos = RichTextField()
    enlaces_formulario = models.URLField(blank=True, null=True)
    imagenes = models.ImageField(upload_to='articulo/',blank=True)
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

class Donaciones(models.Model):
    titulo = models.CharField(max_length=200)
    info_impacto = RichTextField()
    historial = RichTextField()
    donar = RichTextField()
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Donación"
        verbose_name_plural = "Donaciones"

class DonacionesCBU(models.Model):
    banco = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    numero = models.CharField(max_length=255)
    sucursal = models.CharField(max_length=200)
    cbu = models.CharField(max_length=250)
    alias = models.CharField(max_length=150)
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.banco

    class Meta:
        verbose_name = "DonaciónCBU"
        verbose_name_plural = "DonacionesCBU"