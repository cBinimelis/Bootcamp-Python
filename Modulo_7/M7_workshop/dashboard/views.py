from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    # 1. Obtener los datos a partir de una consulta
    # 2 Graficar los datos

    """
    ejemplo SELECT id, precio
    """

    return render(request, "dashboard/home.html")


def execute_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        return [dict(zip(columns, row)) for row in rows]
