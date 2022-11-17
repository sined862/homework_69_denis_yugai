from django.urls import path
from calculator.views import index_view, add_view, subtract_view, multiply_view, divide_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide')
]