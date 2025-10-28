let carrito = [];

function añadirCarrito(producto){
    carrito.push(producto);
    alert(producto + " añadido al carrito");
}

function enviarPedido(){
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;

    fetch('http://127.0.0.1:5000/nuevo-cliente', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nombre, email, pedido: carrito.join(', ')})
    })
    .then(res => res.json())
    .then(data => alert('Pedido enviado con éxito!'))
    .catch(err => console.error(err));
}
