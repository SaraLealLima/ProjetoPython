from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__, template_folder="")


@app.route("/", methods = ["GET", "POST"])
def home():
    
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        calculo = request.form["calculo"]
        
        if (request.form["num1"] == ""):
            return "Preencha o primeiro campo"

        if (request.form["num2"] == ""):
            return "Preencha o segundo campo"
            
        if (request.form["calculo"] == ""):
            return "Escolha uma operação"

             
        
        if (request.form["calculo"] == "soma"):
            soma = int(num1) + int(num2)
            return {
                "Resultado": str(soma) 
            }
            
        elif (request.form["calculo"] == "subtracao"):
            subtracao = int(num1) - int(num2)
            return {
                "Resultado": str(subtracao) 
            }
        elif (request.form["calculo"] == "multiplicacao"):
            multiplicacao = int(num1) * int(num2)
            return {
                "Resultado": str(multiplicacao) 
            }
        elif (request.form["calculo"] == "juros"):
            juros1 = int(num2) / 100
            juros2 = int(num1) * juros1
            juros3 = int(num1) + juros2
            return {
                "Resultado": str(juros3) 
            }   
        elif (request.form["calculo"] == "divisao"):
            divisao = int(num1) // int(num2)
            return {
                "Resultado": str(divisao) 
            }
        else:
            resto = int(num1) % int(num2)
            return {
                "Resultado": str(resto) 
            }

            

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.errorhandler(404)
def not_found(erro):
    return "Insira valores válidos"



app.run(debug=True) 

# mudar a porta: passar o parametro port=0000