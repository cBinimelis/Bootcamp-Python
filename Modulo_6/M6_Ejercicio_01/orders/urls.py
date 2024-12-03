from django.urls import path
from . import views

app_name='orders'

urlpatterns=[
    path('',views.list, name='list'),
    path('detail/',views.detail, name='detail'),
]