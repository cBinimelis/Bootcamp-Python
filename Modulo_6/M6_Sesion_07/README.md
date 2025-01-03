# Modulo VI - Sesión VII

## Agenda

- Formularios en Django

## Formularios en Django

En HTML, un formulario es una colección de elementos dentro de `<form>...</form>` que permiten a un visitante hacer cosas como ingresar texto, seleccionar opciones, manipular objetos o controles, etc., y luego enviar esa información de regreso al servidor.

Además de sus elementos `<input>` , un formulario debe especificar dos cosas:

- **Donde :** la URL a la que deben devolverse los datos correspondientes a la entrada del usuario
- **Cómo :** el método HTTP debe devolver los datos

Cuando se activa el elemento `<input type="submit" value="Log in">` , los datos se devuelven a` /admin/`.
`GET` y `POST` son los únicos métodos HTTP para usar cuando se trata de formularios.

El formulario de inicio de sesión de Django se devuelve utilizando el método `POST`. ``GET`, por el contrario, agrupa los datos enviados en una cadena y los utiliza para componer una URL.

Django se ocupa de tres partes distintas del trabajo relacionado con las formas:

- Preparando y reestructurando los datos para que estén listos para su presentación
- Creando formularios HTML para los datos
- Recibir y procesar los formularios y datos presentados por el cliente

## Forms de Django v/s formularios HTML

Los formularios de Django son una construcción del lado del servidor. Los formularios HTML son una construcción del lado del cliente

### Construyendo un formulario

```HTML
<form action="/your-name" method="post">
    <label for="your_name">Your name:</label>
    <input id="your_name" type="text" name="your_name" value="{{current_name}}">
    <input type="submit" value="OK">
</form>
```

### La clase de form

```python
from django import forms

class NameForm(forms.Form):
    your_name=forms.CharField(label = 'Your name', max_Length=100)
```

### Primera renderización del formulario

```HTML
    <label for="your_name">Your name:</label>
    <input id="your_name" type="text" name="your_name" maxlength='100' required>
```

### Agregando la vista del formulario

```python
from django.http import HttpResponseRedirect
from django.shortcuts import
from .forms import NameForm

def get_name(request):
    # Si se trata de una solicitud POST, necesitamos procesar los datos del formulario.
    if request.method == 'POST':
        # Crear una instancia del formulario y completarla con los datos de la solicitud.
        form = NameForm(request.POST)
        # Comprobar si es válido
        if form.is_valid():
            # Procesar los datos en form.cleaned_data según sea necesario
            # ...
            # ...
            # Redirigir a una nueva URL
            return HttpResponseRedirect('/thanks/')
    # Si es un GET o cualquier otro método de crearemos un formulario en blanco.
    else:
        form = NameForm()

    return render (request, 'name.html',{'form':form})
```

### Agregando el template de despliegue

```HTML
<form action="/your-name" method="post">
  {% csrf_token %}
  {{form}}
  <input type="submit" value="OK" />
</form>
```

### Renderizar los campos de forma manual
