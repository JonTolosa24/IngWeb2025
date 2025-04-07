from django.shortcuts import render, get_object_or_404, render, get_list_or_404
from django.http import HttpResponse
from .models import Empresa, Trabajador, Red, Equipo


def indice(request):   
    empresas = Empresa.objects.order_by('nombre')   
    output = ', '.join([e.nombre for e in empresas]) #join coge el listado y le añade el separador de la coma
    return HttpResponse(output)
#consultar a la bbdd las empresas por nombre

def comprar(request):
    return HttpResponse("He comprado!")

def nombre(request, nombre): 
    return HttpResponse("Consultando la empresa %s." %nombre)  

def detalle_empresa(request, nombre):
    empresa = get_object_or_404(Empresa, nombre=nombre) #con el get_object_or_404 no hace falta hacer el try catch
    trabajadores = empresa.trabajadores.all() 


def trabajadores(request):
    trabajadores= get_list_or_404(Trabajador.objects.order_by("nombre"))
    context = {
        "lista_trabajadores": trabajadores
    }
    return render(request, "trabajador.html", context)
    
def redes(request):
    redes= get_list_or_404(Red.objects.order_by("nombre"))
    context = {
        "lista_redes": redes
    }
    return render (request, "redes.html", context)

def empresas(request):
    empresas= get_list_or_404(Empresa.objects.order_by("nombre"))
    context = {
        "lista_empresas": empresas
    }
    return render (request, "empresas.html", context)

def detalle_trabajador(request, nombre):
    trabajador = get_list_or_404(Trabajador.objects.order_by("nombre"))
    context = {
        "lista_empresas": empresas
    }
    return render (request, "empresas.html", context)

def detalle_trabajador(request, id):
    trabajador = get_object_or_404(Trabajador, pk = id)
    context = {
        "trabajador": trabajador
    }
    return render(request, "trabajador-detalle.html", context)

def empresa_trabajadores(request, nombre_url):           
    empresa = get_object_or_404(Empresa, nombre=nombre_url) 
    
    trabajadores = empresa.trabajadores.all()
    
    context = {
        "empresa": empresa,
        "trabajadores": trabajadores
    }
    return render(request, "empresas-trabajadores.html", context)

def login():
    logging.info("=== LOGIN DE USUARIO ===")
    try:
        with open(USUARIOS_FILE, "r") as f:
            usuarios_data = json.load(f)
    except Exception as e:
        logging.error(f"No se pudo cargar el archivo de usuarios: {e}")
        exit()

    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ").strip()
        contraseña = input("Contraseña: ").strip()
        if usuario in usuarios_data and usuarios_data[usuario]["password"] == contraseña:
            logging.info(f"Login exitoso. Bienvenido, {usuario}")
            return usuario, usuarios_data[usuario]["bucket"]
        else:
            intentos -= 1
            logging.warning(f"Credenciales incorrectas. Intentos restantes: {intentos}")
    logging.error("Demasiados intentos fallidos. Finalizando programa.")
    exit()