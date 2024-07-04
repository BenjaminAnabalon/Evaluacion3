from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Compra, Usuario
from .forms import ProductoForm, UsuarioForm
from django.http import JsonResponse, HttpResponse
import json

def descripcion(request):
    return render(request, 'ev3/descripcion.html')

def descripcion1(request):
    return render(request, 'ev3/descripcion1.html')

def descripcion2(request):
    return render(request, 'ev3/descripcion2.html')

def login(request):
    return render(request, 'ev3/login.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = ProductoForm()
    
    return render(request, 'ev3/agregar_producto.html', {'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ev3/listar_productos.html', {'productos': productos})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        carrito = request.session.get('carrito', {})
        if producto_id in carrito:
            carrito[producto_id]['cantidad'] += 1
        else:
            carrito[producto_id] = {
                'id': producto_id,
                'nombre': producto.nombre,
                'precio': float(producto.precio),
                'cantidad': 1,
            }
        request.session['carrito'] = carrito

        return JsonResponse({'message': 'Producto agregado al carrito.', 'success': True})
    
    return JsonResponse({'error': 'Método no permitido.', 'success': False})

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_carrito = []
    total_carrito = 0
    for key, value in carrito.items():
        subtotal = value['cantidad'] * value['precio']
        total_carrito += subtotal
        productos_carrito.append({
            'id': value['id'],
            'nombre': value['nombre'],
            'precio': value['precio'],
            'cantidad': value['cantidad'],
            'subtotal': subtotal,
        })
    return render(request, 'ev3/carrito.html', {'productos_carrito': productos_carrito, 'total_carrito': total_carrito})

def principal(request):
    productos = Producto.objects.all()
    return render(request, 'ev3/principal.html', {'productos': productos})

def registro(request):
    return render(request, 'ev3/registro.html')

def modificar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ev3/modificar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return redirect('listar_productos')

def procesar_pago(request):
    if request.method == 'POST':
        carrito = json.loads(request.POST.get('carrito'))
        
        for item in carrito:
            titulo = item['titulo']
            cantidad = item['cantidad']
        
            producto = Producto.objects.get(titulo=titulo)
        
            Compra.objects.create(producto=producto, cantidad=cantidad)
        
        response_data = {'message': 'Compra realizada exitosamente.'}
        return JsonResponse(response_data, status=200)
    
    response_data = {'error': 'Método no permitido'}
    return JsonResponse(response_data, status=405)

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'ev3/usuarios.html', {'usuarios': usuarios})

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, 'ev3/editar_usuario.html', {'form': form, 'usuario': usuario})

def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return redirect('lista_usuarios')

def guardar_compra(request):
    if request.method == 'POST':
        productos_json_str = request.POST.get('productos_json', '')
        productos_json = json.loads(productos_json_str)
        
        for producto_data in productos_json:
            nombre_producto = producto_data.get('nombre_producto', '')
            cantidad = producto_data.get('cantidad', 0)

            producto = Producto.objects.get(nombre=nombre_producto)
            
            nueva_compra = Compra(producto=producto, cantidad=cantidad)
            nueva_compra.save()

        return redirect('principal')
    
    return HttpResponse('Error al procesar la compra.')

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    
    return render(request, 'ev3/agregar_usuario.html', {'form': form})


def mostrar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'ev3/mostrar_compras.html', {'compras': compras})