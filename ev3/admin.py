from django.contrib import admin
from .models import Producto, Usuario, Compra

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Compra)