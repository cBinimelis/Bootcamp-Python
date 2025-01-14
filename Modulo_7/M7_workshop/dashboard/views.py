from decimal import Decimal

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection


@login_required
def home(request):
    # 1. Obtener los datos a partir de una consulta
    # 2 Graficar los datos

    """
    ejemplo: SELECT id, price, tax FROM orders

        columns = [id, total]
        rows = [[1,100], [2,200]...]

        [
            {'id': 1, 'total: 100},
            {'id': 2, 'total: 200},
        ]

    """

    query = """
        select o.status, sum((od.price * od.tax) + od.price) as total_venta
        from orders_detail od
        inner join orders_order o on o.id = od.order_id
        group by o.status
    
    """

    data = execute_sql(query)
    data = convert_decimal_to_float(data)

    context = {"data": data}

    return render(request, "dashboard/home.html", context)


def execute_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        return [dict(zip(columns, row)) for row in rows]


def convert_decimal_to_float(data):
    for row in data:
        for key, value in row.items():
            if isinstance(value, Decimal):
                row[key] = float(value)

    return data
