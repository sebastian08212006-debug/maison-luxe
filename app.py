from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # These names MUST match your filenames in the static folder exactly (lowercase)
    maison_collections = [
        {'name': 'The Acroteria Bag', 'image': 'acroteria.jpg'},
        {'name': 'The Sunflower Bag', 'image': 'sunflower.jpg'}
    ]
    return render_template('index.html', collections=maison_collections)

@app.route('/world-of-earl')
def world_of_earl():
    return render_template('world.html')

if __name__ == '__main__':
    app.run(debug=True)
