from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"mensagem":"Olá, API Flask funcionando!"})


if __name__ == "__main__":
    app.run(debug=True)