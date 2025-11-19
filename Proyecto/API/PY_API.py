from flask import Flask, jsonify, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Endpoint para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(data), 200

# Endpoint para obtener un producto por ID
@app.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto_por_id(producto_id):
    producto = next((p for p in data if p['id'] == producto_id), None)
    if producto:
        return jsonify(producto), 200
    return jsonify({"error": "Producto no encontrado"}), 404

# Endpoint para agregar un nuevo producto
@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = request.get_json()
    if not nuevo_producto or 'nombre' not in nuevo_producto or 'precio' not in nuevo_producto:
        return jsonify({"error": "Datos inválidos"}), 400
    nuevo_producto['id'] = len(data) + 1
    data.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

# Endpoint para actualizar un producto existente
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    producto = next((p for p in data if p['id'] == producto_id), None)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
    datos_actualizados = request.get_json()
    producto.update(datos_actualizados)
    return jsonify(producto), 200

# Endpoint para eliminar un producto
@app.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    global data
    data = [p for p in data if p['id'] != producto_id]
    return jsonify({"mensaje": "Producto eliminado"}), 200

# Endpoint para obtener todos los productos
@app.route('/sucursales', methods=['GET'])
def obtener_sucursales():
    return jsonify(suc), 200

# Endpoint para obtener un producto por ID
@app.route('/sucursales/<int:sucursal_id>', methods=['GET'])
def obtener_sucursal_por_id(sucursal_id):
    sucursal = next((p for p in suc if p['id'] == sucursal_id), None)
    if sucursal:
        return jsonify(sucursal), 200
    return jsonify({"error": "Producto no encontrado"}), 404

# Endpoint para agregar un nuevo producto
@app.route('/sucursales', methods=['POST'])
def agregar_sucursal():
    nuevo_sucursal = request.get_json()
    if not nuevo_sucursal or 'nombre' not in nuevo_sucursal or 'precio' not in nuevo_sucursal:
        return jsonify({"error": "Datos inválidos"}), 400
    nuevo_sucursal['id'] = len(data) + 1
    data.append(nuevo_sucursal)
    return jsonify(nuevo_sucursal), 201

# Endpoint para actualizar un producto existente
@app.route('/sucursales/<int:sucursal_id>', methods=['PUT'])
def actualizar_sucursal(sucursal_id):
    sucursal = next((p for p in data if p['id'] == sucursal_id), None)
    if not sucursal:
        return jsonify({"error": "sucursal no encontrada"}), 404
    datos_actualizados = request.get_json()
    sucursal.update(datos_actualizados)
    return jsonify(sucursal), 200

# Endpoint para eliminar un producto
@app.route('/sucursales/<int:sucursal_id>', methods=['DELETE'])
def eliminar_sucursal(sucursal_id):
    global suc
    suc = [p for p in suc if p['id'] != sucursal_id]
    return jsonify({"mensaje": "Sucursal eliminado"}), 200


# Endpoint para obtener todos los productos
@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    return jsonify(cli), 200

# Endpoint para obtener un producto por ID
@app.route('/clientes/<int:cliente_id>', methods=['GET'])
def obtener_cliente_por_id(cliente_id):
    cliente = next((p for p in cli if p['id'] == cliente_id), None)
    if cliente:
        return jsonify(cliente), 200
    return jsonify({"error": "cliente no encontrado"}), 404

# Endpoint para agregar un nuevo producto
@app.route('/clientes', methods=['POST'])
def agregar_cliente():
    nuevo_cliente = request.get_json()
    if not nuevo_cliente or 'nombre' not in nuevo_cliente or 'direccion' not in nuevo_cliente:
        return jsonify({"error": "Datos inválidos"}), 400
    nuevo_cliente['id'] = len(cli) + 1
    data.append(nuevo_cliente)
    return jsonify(nuevo_cliente), 201


# Endpoint para actualizar un producto existente
@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def actualizar_cliente(cliente_id):
    cliente = next((p for p in cli if p['id'] == cliente_id), None)
    if not cliente:
        return jsonify({"error": "cliente no encontrado"}), 404
    datos_actualizados = request.get_json()
    cliente.update(datos_actualizados)
    return jsonify(cliente), 200

# Endpoint para eliminar un producto
@app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def eliminar_cliente(cliente_id):
    global cli
    cli = [p for p in cli if p['id'] != cliente_id]
    return jsonify({"mensaje": "cliente eliminado"}), 200


# Datos simulados (base de datos en memoria)
data = [
    {"id": 1, "descripcion": "Creacion de DataMart", "precio": 100},
    {"id": 2, "descripcion": "Revision de sistema transaccional", "precio": 100},
    {"id": 3, "descripcion": "Revision de sistema", "precio": 500},
    {"id": 4, "descripcion": "Revision de reglas de firewall", "precio": 200},
]

# Datos simulados (base de datos en memoria)
suc = [
    {"id": 1, "descripcion": "Sucursal central", "direccion": "15 avenida 7-49 zona 1"},
    {"id": 2, "descripcion": "Sucursal metronorte", "direccion": "metronorte 4-56 zona 18"},
    {"id": 3, "descripcion": "sucursal petapa", "direccion": "avenida petapa 11-31 zona 12"},
    {"id": 4, "descripcion": "sucursal zona 6", "direccion": "15 avenida 7-49 zona 6"},
]

# Datos simulados (base de datos en memoria)
cli = [
    {"id": 1, "nombre": "Empresa S.A.", "direccion": "15 avenida 7-49 zona 1","cliente":"","lat":"14.3216","long":"-14.2235"},
    {"id": 2, "nombre": "Ministerio de Agricultura", "direccion": "15 avenida 7-49 zona 1","cliente":"","lat":"10.14487","long":"11.4897"},
    {"id": 3, "nombre": "Empresa de papel S.A.", "direccion": "15 avenida 7-49 zona 1","cliente":"","lat":"11.47794","long":"-13.44484"},
    {"id": 4, "nombre": "Empresa IMP S.A.", "direccion": "15 avenida 7-49 zona 1","cliente":"","lat":"17.1154","long":"-11.11486"},
]

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)