function getProductos() {
    fetch('/api/productos')
    .then(res => res.json())
    .then(data => {
        const tbody = document.querySelector('#product-list tbody');
        tbody.innerHTML = '';
        data.forEach(p => {
            const row = `
            <tr>
            <td>${p.nombre}</td>
            <td>${p.descripcion}</td>
            <td>${p.precio}</td>
            <td>${p.cantidad}</td>
            <td>
            <button class="btn btn-sm btn-warning" onclick="editProducto(${p.id})">Editar</button>
            <button class="btn btn-sm btn-danger" onclick="deleteProducto(${p.id})">Eliminar</button>
            </td>
            </tr>`;
            tbody.innerHTML += row;
        });
    });
}

function createProducto() {
    const data = {
        nombre: document.getElementById('nombre').value,
        descripcion: document.getElementById('descripcion').value,
        precio: parseFloat(document.getElementById('precio').value),
        cantidad: parseInt(document.getElementById('cantidad').value)
    };

    fetch('/api/productos', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(r => r.json())
    .then(() => getProductos());
}

function editProducto(id) {
    window.location.href = `/edit_producto/${id}`;
}

function updateProducto() {
    const id = document.getElementById('product-id').value;
    const data = {
        nombre: document.getElementById('nombre').value,
        descripcion: document.getElementById('descripcion').value,
        precio: parseFloat(document.getElementById('precio').value),
        cantidad: parseInt(document.getElementById('cantidad').value)
    };

    fetch(`/api/productos/${id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(() => window.location.href = '/productos');
}

function deleteProducto(id) {
    if (!confirm('¿Eliminar producto?')) return;
    fetch(`/api/productos/${id}`, { method: 'DELETE' })
    .then(() => getProductos());
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("Página cargada correctamente");
});
