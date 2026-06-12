from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def concierto():
    return jsonify({
        "festival": "Pacific DevOps Music Fest 2026",
        "fecha": "20 de diciembre de 2026",
        "artistas": [
            "Neutro Shorty",
            "La Más Doll",
            "Danny Ocean"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
