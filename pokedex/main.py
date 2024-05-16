from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def get_pokemon_info():
    # If the request method is POST, then the form has been submitted
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            id = pokemon_data['id']
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']
            types = [t['type']['name'] for t in pokemon_data['types']]
            image_url = pokemon_data['sprites']['front_default']
            return render_template('pokemon_info.html', id=id, name=name, height=height, weight=weight, types=types, image_url=image_url)
        else:
            return "Error: Failed to retrieve Pokemon information."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)