from flask import Flask, render_template, request, flash

app = Flask(__name__)

# Establecer una clave secreta
app.secret_key = '1234'

# Resto de tu código Flask
@app.route("/hello")
def index():
    flash("Inserte tus deseos")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']))
    return render_template("index.html")