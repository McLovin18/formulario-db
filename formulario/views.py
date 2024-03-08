from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import FormularioForm

def formulario_view(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            nombre = datos['nombre']
            apellido = datos['apellido']
            email = datos['email']
            asunto = datos['asunto']
            mensaje = datos['mensaje']

            # Utiliza el nombre y el apellido como el remitente del correo electrónico
            remitente = f"{nombre} {apellido} <{email}>"


            # Enviar correo electrónico
            contenido = f"Nombre: {nombre} {apellido}\nCorreo electrónico: {email}\nAsunto: {asunto}\n\nMensaje:\n{mensaje}"
            send_mail(
                f'Formulario de Contacto - {asunto}',
                contenido,
                remitente,
                ['hectorcobea03@gmail.com'],
                fail_silently=False,
            )

            form.save()
            return redirect('exito')
    else:
        form = FormularioForm()
    return render(request, 'formulario.html', {'form': form})

def exito_view(request):
    return render(request, 'exito.html')
