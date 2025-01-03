# Modulo VI - Sesión IX

## Agenda

- Autorización y permisos

## Autorización y permisos

### ¿En qué consiste el modelo de permisos Django?

El sitio de administración de Django usa permisos de la siguiente manera:

- El acceso para ver objetos está limitado a los usuarios con el permiso de "ver" o "cambiar" para ese tipo de objeto.
- El acceso para ver el formulario "agregar" y agregar un objeto está limitado a los usuarios con el permiso "agregar" para ese tipo de objeto.
- El acceso para ver la lista de cambios, ver el formulario de "cambio" y cambiar un objeto está limitado a los usuarios con el permiso de "cambio" para ese tipo de objeto.
- El acceso para eliminar un objeto está limitado a los usuarios con el permiso de "eliminación" para ese tipo de objeto.

En caso de que se requiera probar la permisología básica que pueda tener un usuario se debe usar: (asumiendo que tenemos una aplicación llamada auto y un modelo llamado Ford)

- add: `user.has_perm('auto.add_ford')`
- change: `user.has_perm('auto.change_ford')`
- delete: `user.has_perm('auto.delete_ford')`
- view: `user.has_perm('auto.view_ford')`

- **GRUPOS:** Los grupos son una forma genérica de trabajar con varios usuarios a la vez, de forma que se les pueda asignar permisos o etiquetas en bloque.
- **USO DE MIXINS:** Hacer uso de mixins puede proporcionar una gran funcionalidad no solo para los modelos de base de datos, sino también para otras clases que pueda tener.
- **APLICANDO LOGINREQUIERDMIXIN:** Al utilizar vistas basadas en clases, puede lograr el mismo comportamiento que con login_required haciendo uso de LoginRequiredMixin.

  ```python
  from django.contrib.auth.mixins import LoginRequiredMixin

  class MyView(LoginRequiredMixin, View):
      login_url = '/login/'
      redirect_field_name = '/redirect_to/'
  ```

- **APLICANDO PERMISSIONREQUIREDMIXIN:** Para aplicar verificaciones de permisos a vistas basadas en clases, se puede utilizar PermissionRequiredMixin, este mixin, al igual que allow_required, verifica si el usuario que accede a una vista tiene todos los permisos otorgados.

  ```python
  from django.contrib.auth.mixins import PermissionRequiredMixin

  class MyView(PermissionRequiredMixin, View):
      permission_required = 'polls.add_choice'
      # O múltiples permisos:
      permission_required = ('polls.view_choice', 'polls.change_choice')
  ```

Examinando la tabla auth_permissions: Como ya hemos visto, Django cuenta con una función de permisos. Luego de crear un modelo, existen cuatro tipos de permisos para ese modelo de forma predeterminada, estos son:

- add (agregar)
- delete (eliminar)
- change (cambiar)
- view (visualizar)

Todos estos permisos se pueden ver en la tabla auth_permission de la base de datos, luego de ejecutar el comando migrate.

En caso de requerir añadir un permiso adicional, por ejemplo editar, éste se puede especificar utilizando el atributo permission en la clase Meta, de la siguiente manera

```python
class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    manufacture = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    class Meta:
        permissions = (('edit_car','can edit car'),)
```

- **Redireccionando los accesos no autorizados:** La manera indicada de limitar el acceso a las páginas del sistema es chequear `request.user.is_authenticated`

  ```python
  from django.conf import settings
  from django.shortcuts import redirect

  def MyView(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
  ```

  ```python
    from django.shortcuts import render
    def my_view(request):
        if not request.user.is_authenticated:
            return render(request, 'app/login_error.html')
  ```

- **Vistas de autenticación:** Django ofrece un conjunto de vistas para el manejo de inicio de sesión (login), cierre de sesión (logout) y administración de contraseñas.

  ```python
    urlpatterns = [
        path('accounts/', include('django.contrib.auth.urls')),
    ]
  ```
