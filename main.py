from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def index1():
    return render_template("alumnos.html")

@app.route("/maestros")
def index2():
    return render_template("maestros.html")

@app.route("/hola")
def func():
    return "<h1>Saludo desde Hola - UTL!!</1>"

@app.route("/saludo")
def func1():
    return "<h1>Saludo desde Saludo</1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1>Hola </1>" + nom

@app.route("/numero/<int:num>")
def numero(num):
    return "<h1>El valor es {} </1>".format(num)

@app.route("/user/<string:nom>/<int:id>")
def user(nom, id):
    return "<h1>El usuario es: {} y el id {} </1>".format(nom, id) 

@app.route("/suma/<float:n1>/float:n2>")
def suma(n1, n2):
    return "<h1>La suma de {} + {} = {} </1>" .format(n1,n2, n1+n2)

@app.route("/multiplicar", methods=["GET", "POST"])
def multi():
    if request.method =="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1>El resultado es: {}</h1>".format(str(int(num1)*int(num2)))
    else:
        return '''
                <form action = "/multiplicar" method = "POST">
                    <label>N1:</label>
                    <input type="text" name="n1"/>
                    <label>N2:</label>
                    <input type="text" name="n2"/>
                    <input type="submit">
                </form>
                '''

@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET", "POST"])
def multi1():
    if request.method =="POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1>El resultado es: {}</h1>".format(str(int(num1)*int(num2)))

if __name__ =="__main__":
    app.run(debug=True)
    