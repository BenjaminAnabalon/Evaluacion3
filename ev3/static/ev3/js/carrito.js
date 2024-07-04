$(document).ready(function() {
    // Función para cargar y mostrar el carrito desde localStorage
    function mostrarCarrito() {
        var carrito = JSON.parse(localStorage.getItem('carrito')) || [];

        // Limpiar el cuerpo de la tabla antes de llenarla
        $('#tbody-carrito').empty();

        // Iterar sobre los productos en el carrito y agregar filas a la tabla
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

        // Si no hay productos en el carrito, mostrar mensaje de carrito vacío
        if (carrito.length === 0) {
            var filaVacia = `
                <tr>
                    <td colspan="5">Tu carrito está vacío.</td>
                </tr>
            `;
            $('#tbody-carrito').append(filaVacia);
        }
    }

    // Evento para incrementar la cantidad
    $(document).on('click', '.btn-incrementar', function() {
        var inputCantidad = $(this).siblings('.input-cantidad');
        var cantidadActual = parseInt(inputCantidad.val());
        if (cantidadActual < 10) {
            inputCantidad.val(cantidadActual + 1);
            actualizarCantidadProducto(inputCantidad);
        }
    });

    // Evento para decrementar la cantidad
    $(document).on('click', '.btn-decrementar', function() {
        var inputCantidad = $(this).siblings('.input-cantidad');
        var cantidadActual = parseInt(inputCantidad.val());
        if (cantidadActual > 1) {
            inputCantidad.val(cantidadActual - 1);
            actualizarCantidadProducto(inputCantidad);
        } else {
            // Si la cantidad llega a 0, eliminar el producto del carrito
            var producto_id = inputCantidad.closest('tr').find('.btn-eliminar-producto').data('producto-id');
            eliminarProducto(producto_id);
        }
    });

    // Evento para eliminar un producto del carrito
    $(document).on('click', '.btn-eliminar-producto', function() {
        var producto_id = $(this).data('producto-id');
        eliminarProducto(producto_id);
    });

    // Función para actualizar la cantidad de un producto en el carrito
    function actualizarCantidadProducto(inputCantidad) {
        var nuevaCantidad = parseInt(inputCantidad.val());
        var producto_id = inputCantidad.closest('tr').find('.btn-eliminar-producto').data('producto-id');
        var carrito = JSON.parse(localStorage.getItem('carrito')) || [];

        // Actualizar la cantidad del producto en el carrito
        carrito = carrito.map(function(producto) {
            if (producto.id === producto_id) {
                producto.cantidad = nuevaCantidad;
            }
            return producto;
        });

        // Guardar el carrito actualizado en localStorage
        localStorage.setItem('carrito', JSON.stringify(carrito));

        // Mostrar nuevamente el carrito actualizado
        mostrarCarrito();
    }

    // Función para eliminar un producto del carrito
    function eliminarProducto(producto_id) {
        var carrito = JSON.parse(localStorage.getItem('carrito')) || [];

        // Filtrar el producto a eliminar del carrito
        carrito = carrito.filter(function(producto) {
            return producto.id !== producto_id;
        });

        // Guardar el carrito actualizado en localStorage
        localStorage.setItem('carrito', JSON.stringify(carrito));

        // Mostrar nuevamente el carrito actualizado
        mostrarCarrito();
    }

    // Mostrar inicialmente el carrito al cargar la página
    mostrarCarrito();
});
