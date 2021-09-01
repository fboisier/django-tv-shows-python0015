from django.shortcuts import render, redirect
from app.models import Show
from django.contrib import messages

def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        'programas_tv' : Show.objects.all(),
        'variable' : Show.objects.saludar("Francisco")
    }
    return render(request, 'shows.html', context)

def agregar(request):
    context = {}
    return render(request, 'agregar.html', context)

def editar(request, id):
    context = {
        'id' : id
    }
    return render(request, 'editar.html', context)

def show(request, id):
    context = {
        'id' : id
    }
    return render(request, 'mostrar.html', context)

def borrar(request, id):
    context = {
        'id' : id
    }
    return render(request, 'borrar.html', context)


def crear_show(request):
    print(request.POST)

    errores = Show.objects.validador(request.POST)
    
    if len(errores) > 0:
        for key, value in errores.items():
            messages.error(request, value + " Code: " + key)

        request.session['show_title'] = request.POST['title']
        request.session['show_network'] = request.POST['network']
        request.session['show_release'] = request.POST['release']
        request.session['show_description'] = request.POST['description']
        
        
        return redirect("/shows/new")
    else:

        request.session['show_title'] = ""
        request.session['show_network'] = ""
        request.session['show_release'] = ""
        request.session['show_description'] = ""

        show = Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release'],
                description=request.POST['description'],
            )

        messages.success(request, "Fue un exito agregar el titulo " + show.title)
        return redirect(f"/shows/{show.id}")

