from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template

def familia(request):
    return HttpResponse('<h2>Esta es solo una pequeña muestra del universo que es toda mi familia (vaya que es grande, somos como 80). </h2>')

def template(request):
    cargar_archivo = open(r'C:\Users\pc\CAFECO ICOSA CGSSUR Dropbox\Raúl Galeana\Educacion continua\Programacion\220725_CoderHouse_Python\Desafio-S10\templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    template_render = template.render(contexto)
    
    return HttpResponse(template_render)