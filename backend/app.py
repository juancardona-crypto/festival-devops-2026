from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Festival DevOps Music Fest API'})

@app.route('/artistas')
def artistas():
    return jsonify({'artistas': ['Imagine Dragons', 'The Warning', 'Daft Punk']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
