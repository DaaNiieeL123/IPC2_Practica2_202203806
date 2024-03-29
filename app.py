from flask import Flask
from flask import request, jsonify, render_template
import webbrowser
from DatosClientes.clientes import *
from DatosClientes.Ayuda import *

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de Registro
@app.route('/registro')
def registro():
    return render_template('registro.html')

# Ruta para la página de Eliminar
@app.route('/eliminar')
def eliminar():
    return render_template('eliminar.html')

@app.route('/ayuda')
def ayuda():
    nombres_data = nombres()
    apellidos_data = apellidos()
    carnet_data = carnet()
    practica_data = practica()
    enlace_data = enlance()
    return render_template('ayuda.html', nombres=nombres_data, apellidos=apellidos_data, carnet=carnet_data, practica=practica_data, enlace=enlace_data)


gestor_clientes = GestorClientes()

# Ruta para crear un cliente
@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['Correo']
    nit = request.form['nit']

    resultado = gestor_clientes.registrar_cliente(nombre, apellido, correo, nit)
    if resultado == 'registrado':
        mensaje = f'EL Cliente {nombre}, ha sido registrado correctamente.'
    elif resultado == 'existente':
        mensaje = f'Ya existe un Cliente con NIT {nit}, registrado en el Sistema.\n'
        mensaje += 'Por favor, verifique el NIT e intente nuevamente.'
    else:
        mensaje = 'Error: No se pudo registrar el cliente.'

    return render_template('registro.html', mensaje=mensaje)

# Ruta para obtener los clientes
@app.route('/getclientes')
def mostrarClientes():
    lista_clientes = gestor_clientes.obtener_clientes()
    return render_template('clientes.html', clientes=lista_clientes)

@app.route('/eliminarCliente', methods=['POST'])
def eliminar_cliente():
    nit = request.form['nit']

    cliente_eliminado = gestor_clientes.eliminar_cliente(nit)
    if cliente_eliminado:
        mensaje = f'El Cliente {cliente_eliminado.nombre}, NIT {nit} , ha sido Eliminado Correctamente.'
    else:
        mensaje = f'No Existe un Cliente con este NIT{nit}.'

    return render_template('eliminar.html', mensaje=mensaje, clientes=gestor_clientes.obtener_clientes())


# Abre automáticamente el navegador predeterminado con la dirección de tu aplicación Flask
webbrowser.open('http://127.0.0.1:5000/registro')

if __name__ == '__main__':
    app.run(debug=True)
