from tamagotchi import Tamagotchi
from flask import Flask, render_template, jsonify


app = Flask(__name__)

tama = Tamagotchi("mojonapower")
# print(tama.crecer())
# print(tama.crecer())
# print(tama.crecer())
# print(tama.crecer())

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html', tama = tama.serialize() )

@app.route("/crecer", methods=['GET'])
def comer():
    mensaje = tama.crecer()
    return jsonify({
        "mensaje":mensaje
    })

@app.route("/status", methods=['GET'])
def show_status():
    return jsonify(tama.serialize())
if __name__ =='__main__': #estoy definiendo que este es el archivo principal
    app.run(debug=True)
