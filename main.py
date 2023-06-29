from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Fala Galera!</h1><h3>OK</h3>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
