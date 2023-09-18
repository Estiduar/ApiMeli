from flask import Flask, request, render_template, jsonify
import requests
import random

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

# Ruta para obtener el tipo de un Pokémon por su nombre (GET)
@app.route('/pokemon/tipo/<nombre>', methods=['GET'])
def obtener_tipo_pokemon(nombre):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        tipos = [tipo['type']['name'] for tipo in data['types']]
        return render_template('infopokeapi.html', nombre=nombre, tipos=tipos)
    else:
        return jsonify({'error': 'No se encontró el Pokémon'}), 404

# Ruta para obtener un Pokémon al azar de un tipo en específico (GET)
@app.route('/pokemon/azar/<tipo>', methods=['GET'])
def obtener_pokemon_azar(tipo):
    url = f'https://pokeapi.co/api/v2/type/{tipo.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemons = data['pokemon']
        pokemon_azar = random.choice(pokemons)['pokemon']['name']
        return render_template('infopokeapi.html', pokemon_azar=pokemon_azar)
    else:
        return jsonify({'error': 'No se encontró el tipo de Pokémon'}), 404

# Ruta para obtener el Pokémon con el nombre más largo de cierto tipo (GET)
@app.route('/pokemon/maslargo/<tipo>', methods=['GET'])
def obtener_pokemon_mas_largo(tipo):
    url = f'https://pokeapi.co/api/v2/type/{tipo.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemons = data['pokemon']
        pokemon_mas_largo = max(pokemons, key=lambda x: len(x['pokemon']['name']))['pokemon']['name']
        return render_template('infopokeapi.html', pokemon_mas_largo=pokemon_mas_largo)
    else:
        return jsonify({'error': 'No se encontró el tipo de Pokémon'}), 404

if __name__ == "__main__":
   app.run(host="localhost", port=5000, debug=True)


