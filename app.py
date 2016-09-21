from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "choose a tropical fruit: <br>/rambutan <br>/mangosteen <br>/durian"

@app.route("/rambutan")
def ramb():
    return "this is a rambutan"

@app.route("/mangosteen")
def mang():
    return "this is a mangosteen"

@app.route("/durian")
def duri():
    return "durians are okay"

if __name__ == "__main__":
    app.run()
