from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm, DonacionForm
import logging
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from .models import Inicio, Nosotros, Programas, Actividades, Historias, Articulos, Donaciones, DonacionesCBU, NosotrosQueBuscamos

logger = logging.getLogger('django')

def inicio(request):
    try:
        inicio_data = Inicio.objects.filter(publicado=True).latest('fecha_publicacion')
    except ObjectDoesNotExist:
        inicio_data = None  # o puedes asignar un valor por defecto o una estructura vacía
    
    try:
        nosotros_data = Nosotros.objects.filter(publicado=True).latest('id')  # Obtener el último registro
    except ObjectDoesNotExist:
        nosotros_data = None
        
    #context = {
    #    'inicio': inicio_data,
    #    'nosotros': nosotros_data,
    #}

    return render(request, 'core/inicio.html', {'inicio': inicio_data})

def nosotros(request):
    try:
        nosotros_data = Nosotros.objects.filter(publicado=True).latest('id')  # Obtener el último registro
    except Nosotros.DoesNotExist:
        nosotros_data = None
        
    try:
        busqueda_data = NosotrosQueBuscamos.objects.filter(publicado=True).all()
    except NosotrosQueBuscamos.DoesNotExist:
        busqueda_data = None
    
    #return render(request, 'core/nosotros.html', {'nosotros': nosotros_data})

    return render(request, 'core/nosotros.html', {
        'nosotros': nosotros_data,
        'busqueda_data': busqueda_data
    })

#def nosotros_busqueda(request):
#    try:
#        busqueda_data = NosotrosQueBuscamos.objects.filter(publicado=True).all()
#    except NosotrosQueBuscamos.DoesNotExist:
#        busqueda_data = None
#    
#    return render(request, 'core/nosotros.html', {'busqueda_data': busqueda_data})

def programas(request):
    try:
        programas_data = Programas.objects.filter(publicado=True).latest('id')
    except ObjectDoesNotExist:
        programas_data = None
        
    return render(request, 'core/programas.html', {'programas': programas_data})

def actividad_detalle(request, id):
    actividad = get_object_or_404(Actividades, id=id)
    return render(request, 'core/actividad_detalle.html', {'actividad': actividad})

def actividades(request):
    try:
        actividades_data = Actividades.objects.filter(publicado=True).all()
    except ObjectDoesNotExist:
        actividades_data = None
        
    return render(request, 'core/actividades.html', {'actividades': actividades_data})

def historias(request):
    try:
        historias_data = Historias.objects.filter(publicado=True).all()
    except ObjectDoesNotExist:
        historias_data = None
    
    return render(request, 'core/historias.html', {'historias': historias_data})

def articulos(request):
    try:
        articulos_data = Articulos.objects.filter(publicado=True).all()
    except ObjectDoesNotExist:
        articulos_data = None
        
    return render(request, 'core/articulos.html', {'articulos': articulos_data})

#def donaciones_cbu(request):
#    donaciones_data_cbu = DonacionesCBU.objects.all()
#    return render(request, 'core/donaciones.html', {'donaciones_cbu':donaciones_data_cbu})

def donaciones(request):
    try:
        donaciones_data = Donaciones.objects.filter(publicado=True).latest('id')  # Obtener el último registro de donaciones
    except ObjectDoesNotExist:
        donaciones_data = None
    
    try:
        donaciones_data_cbu = DonacionesCBU.objects.filter(publicado=True).all()
    except ObjectDoesNotExist:
        donaciones_data_cbu = None
    
    form = ContactoForm()  # Inicializar el formulario aquí
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            try:
                # Procesa el formulario y envía el correo electrónico
                nombre = form.cleaned_data['nombre']
                email = form.cleaned_data['email']
                mensaje = form.cleaned_data['mensaje']
                send_mail(
                    'Nuevo mensaje de contacto',
                    f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                    'futurarsinbarreras@gmail.com',  # Cambia esto por el correo desde el cual enviarás el mensaje
                    ['futurarsinbarreras@gmail.com',email],  # Cambia esto por el correo al cual enviarás el mensaje
                    fail_silently=False,
                )
                # redirigir a una url con exito:
                return redirect('contacto_exito')
            except Exception as e:
                logger.error(f"Error al enviar el mensaje de donaciones: {str(e)}")
                # redirigir si falla el envio:
                return redirect('contacto_fallo')
        else:
            form = ContactoForm()

    context = {
        'donaciones': donaciones_data,
        'donaciones_cbu': donaciones_data_cbu,
        'form': form,
        #'mensaje_exito': mensaje_exito,
    }

    return render(request, 'core/donaciones.html', context)

def contacto(request):
    # mensaje_exito = False  # Variable para indicar si se envió el formulario correctamente

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            try:
                
                # Procesa el formulario y envía el correo electrónico
                nombre = form.cleaned_data['nombre']
                email = form.cleaned_data['email']
                mensaje = form.cleaned_data['mensaje']
                send_mail(
                    f'Nuevo mensaje de {nombre}',
                    f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                    'futurarsinbarreras@gmail.com',  # Cambia esto por el correo desde el cual enviarás el mensaje
                    ['futurarsinbarreras@gmail.com',email],  # Cambia esto por el correo al cual enviarás el mensaje
                    fail_silently=False,
                )
                # redirigir a una url con exito:
                return redirect('contacto_exito')
            except Exception as e:
                logger.error(f"Error al enviar el mensaje de {nombre}: {str(e)}")
                # redirigir si falla el envio:
                return redirect('contacto_fallo')
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {'form': form})

def contacto_exito(request):
    return render(request, 'core/contacto_exito.html')

def contacto_fallo(request):
    return render(request, 'core/contacto_fallo.html')