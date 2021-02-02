from flask import Flask, render_template, request
import calculos

app = Flask(__name__, template_folder="")

@app.route("/", methods = ["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and request.form["num2"] != ""):
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            calculo = request.form["calculo"]

            return calculos.calcular(num1, num2, calculo)
            
        else:
            return "Informe valores válidos"

@app.errorhandler(404)
def not_found(erro):
    return "Insira valores válidos"

app.run(debug=True) 
# mudar a porta: passar o parametro port=0000