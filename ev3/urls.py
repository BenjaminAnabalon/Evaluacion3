from django.urls import path
from . import views

urlpatterns = [
    path('descripcion/', views.descripcion, name='descripcion'),
    path('descripcion1/', views.descripcion1, name='descripcion1'),
    path('descripcion2/', views.descripcion2, name='descripcion2'),
    path('login/', views.login, name='login'),
    path('principal/', views.principal, name='principal'),
    path('registro/', views.registro, name='registro'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('agregar_al_carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('productos/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('productos/modificar/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('principal/', views.principal, name='principal'),
    path('productos/modificar/<int:pk>/', views.modificar_producto, name='modificar_producto'),
    path('procesar_pago/', views.procesar_pago, name='procesar_pago'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('agregar-al-carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('guardar-compra/', views.guardar_compra, name='guardar_compra'),
    path('mostrar-compras/', views.mostrar_compras, name='mostrar_compras'),
    path('panel-de-control/', views.panel_de_control, name='panel_de_control'),
    path('panel-de-control/listar-usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('panel-de-control/listar-productos/', views.listar_productos, name='listar_productos'),
    path('panel-de-control/mostrar-compras/', views.mostrar_compras, name='mostrar_compras'),

    
    ]





