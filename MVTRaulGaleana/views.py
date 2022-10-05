from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader

from ver_familia.models import Subfamilia

def alta_familiar(request, apellidos, asignacion, invitados):
    
    sub_familia = Subfamilia(apellidos=apellidos, asignacion=asignacion, invitados=invitados, fecha_pago=datetime.now())
    sub_familia.save()
    
    template = loader.get_template('alta_familiar.html')
    template_render = template.render({'sub-familia': sub_familia})
        
    return HttpResponse(template_render)

def fiesta_familia(request):
    
    sub_familias = Subfamilia.objects.all()
    
    template = loader.get_template('fiesta_familia.html')
    template_rend = template.render({'sub_familias': sub_familias})
    
    return HttpResponse(template_rend)