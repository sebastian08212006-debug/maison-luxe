from flask import Flask, render_template

app = Flask(__name__)

# Artist/Designer Gallery Data (From Earl Gariando's Collection)
maison_collections = [
    {
        "id": "acroteria",
        "name": "The Acroteria Bag",
        "tagline": "Repoussè Metalwork",
        "description": "Exquisite repoussè brass dipped in sterling silver and 24k gold. A masterpiece of architectural wearable art.",
        "image": "acroteria.jpg"
    },
    {
        "id": "sunflower",
        "name": "The Sunflower Bag",
        "tagline": "Nature in Brass",
        "description": "Repousse brass applique in spliced sunflower motif dipped in 24k gold set on handwoven abaca and ticog fibers with mother of pearl clasp.",
        "image": "sunflower.jpg"
    }
]

@app.route('/')
def index():
    return render_template('index.html', collections=maison_collections)

if __name__ == '__main__':
    app.run(debug=True)