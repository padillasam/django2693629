from django.shortcuts import render
from . models import Usuario
from . forms import FormularioUsuario
# Create your views here.
# def usuariolist(request):
#     return render(request,'usuariolist.html')

def usuariolist(request):
    get_usuarios=Usuario.objects.all()
    data={
        'get_usuarios':get_usuarios
    }
    return render(request,'usuariolist.html',data)

def indexFormulario(request):
    usuario=FormularioUsuario()
    return render(request, "formusuario.html",{"form":usuario})

def procesarFormulario(request):
    
    if 'guardar' in request.POST:        
        usuario=FormularioUsuario(request.POST,request.FILES)
        if usuario.is_valid():
            usuario.save()
            usuario=FormularioUsuario()
        return render(request,"formusuario.html",{"form":usuario,"mensaje":"ok"} )
    
    #***** Este if funciona si se llenan los inputs
    #***** Porque en el modelo no son nulos ni blanks
    #****** eejmplo:  my_field = models.CharField(blank=True, null=True, length=500)
    # if 'regresar' in request.POST:
    # #else:
    #     print('ingreso al else')
    #     get_usuarios=Usuario.objects.all()
    #     data={
    #     'get_usuarios':get_usuarios
    #     }
    #     return render(request,'usuariolist.html',data)
