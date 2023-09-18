from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder='template')  # still relative to module

# Lista para almacenar los usuarios registrados (solo para fines de demostración)
usuarios_registrados = []

# Ruta para la página de registro (GET)
@app.route('/registro', methods=['GET'])
def mostrar_formulario_registro():
    return render_template('registro.html')

# Ruta para registrar un usuario (POST)
@app.route('/registro', methods=['POST'])
def registrar_usuario():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    contrasena = request.form.get('contrasena')

    # Aquí puedes realizar la lógica de registro, como guardar los datos en una base de datos
    # En este ejemplo, simplemente los agregaremos a la lista de usuarios registrados
    usuarios_registrados.append({'nombre': nombre, 'email': email, 'contrasena': contrasena})

    return jsonify({'mensaje': 'Usuario registrado correctamente'})

# Ruta para obtener todos los usuarios (GET)
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios_registrados)

if __name__ == "__main__":
   app.run(host="localhost",port=5000, debug=True)