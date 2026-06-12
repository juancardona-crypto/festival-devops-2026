from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Festival DevOps Music Fest API'})

@app.route('/artistas')
def artistas():
    return jsonify({'artistas': ['Imagine Dragons', 'The Warning', 'Daft Punk', 'Maneskin']})
    
@app.route('/prices')
def prices():
    return jsonify({'prices': {'VIP': 200, 'General': 100}})

@app.route('/contacto')
def contacto():
    return jsonify({'contacto': {'email': 'info@festivaldevops.com', 'telefono': '300 123 4567'}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
