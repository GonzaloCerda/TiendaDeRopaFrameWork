$(document).click(function() {
    $.getJSON('http://127.0.0.1:8000/api/lista_producto', function(data) {
        var producto = data;

        $.each(producto, function(i, item) {
            $('#producto').append(
                "<tr><td>" + item.nombreProducto +
                "</td><td>" + item.precio +
                "</td><td>" + item.stock +
                "</td><td>" + item.talla +
                "</td><td>" + item.imgProducto +
                "</td><td>" + item.catalogo + "</td></tr>");

        });


    }).fail(function() {
        console.log('Error al consumir la API!');
    });

});