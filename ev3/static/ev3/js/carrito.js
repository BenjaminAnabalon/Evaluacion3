$(document).ready(function() {
    function mostrarCarrito() {
        var carrito = JSON.parse(localStorage.getItem('carrito')) || [];

        $('#tbody-carrito').empty();

        carrito.forEach(function(producto) {
            var subtotal = producto.precio * producto.cantidad;
            var fila = `
                <tr>
                    <td>${producto.nombre}</td>
                    <td>$${producto.precio.toFixed(2)}</td>
                    <td>
                        <div class="input-group">
                            <button class="btn btn-outline-secondary btn-decrementar" type="button">-</button>
                            <input type="number" class="form-control input-cantidad" value="${producto.cantidad}" min="1" max="10">
                            <button class="btn btn-outline-secondary btn-incrementar" type="button">+</button>
                        </div>
                    </td>
                    <td>$${subtotal.toFixed(2)}</td>
                    <td>
                        <button class="btn btn-outline-danger btn-eliminar-producto" data-producto-id="${producto.id}">Eliminar</button>
                    </td>
                </tr>
            `;
            $('#tbody-carrito').append(fila);
        });
        if (carrito.length === 0) {
            var filaVacia = `
                <tr>
                    <td colspan="5">Tu carrito está vacío.</td>
                </tr>
            `;
            $('#tbody-carrito').append(filaVacia);
        }
    }
    $(document).on('click', '.btn-incrementar', function() {
        var inputCantidad = $(this).siblings('.input-cantidad');
        var cantidadActual = parseInt(inputCantidad.val());
        if (cantidadActual < 10) {
            inputCantidad.val(cantidadActual + 1);
            actualizarCantidadProducto(inputCantidad);
        }
    });
    $(document).on('click', '.btn-decrementar', function() {
        var inputCantidad = $(this).siblings('.input-cantidad');
        var cantidadActual = parseInt(inputCantidad.val());
        if (cantidadActual > 1) {
            inputCantidad.val(cantidadActual - 1);
            actualizarCantidadProducto(inputCantidad);
        } else {
            var producto_id = inputCantidad.closest('tr').find('.btn-eliminar-producto').data('producto-id');
            eliminarProducto(producto_id);
        }
    });
    $(document).on('click', '.btn-eliminar-producto', function() {
        var producto_id = $(this).data('producto-id');
        eliminarProducto(producto_id);
    });
    function actualizarCantidadProducto(inputCantidad) {
        var nuevaCantidad = parseInt(inputCantidad.val());
        var producto_id = inputCantidad.closest('tr').find('.btn-eliminar-producto').data('producto-id');
        var carrito = JSON.parse(localStorage.getItem('carrito')) || [];

        carrito = carrito.map(function(producto) {
            if (producto.id === producto_id) {
                producto.cantidad = nuevaCantidad;
            }
            return producto;
        });

        localStorage.setItem('carrito', JSON.stringify(carrito));

        mostrarCarrito();
    }

    function eliminarProducto(producto_id) {
        var carrito = JSON.parse(localStorage.getItem('carrito')) || [];

        carrito = carrito.filter(function(producto) {
            return producto.id !== producto_id;
        });

        localStorage.setItem('carrito', JSON.stringify(carrito));

        mostrarCarrito();
    }

    mostrarCarrito();
});
