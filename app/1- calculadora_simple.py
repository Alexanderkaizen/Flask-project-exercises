from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hola Mundo'



@app.route('/calculadora/<operation>/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
def calculadora(num1,num2,num3,num4,operation):
    if operation == "suma":
        return f" La suma de como resultado: {num1 + num2 + num3 + num4}"
    elif operation == "resta":
        return f" La resta da como resultado: {num1 - num2 - num3 - num4}"
    elif operation == "multiplicacion":
        return f" La multiplicacion da como resultado: {num1 * num2  *num3 *num4} "
    elif operation == "divicion":
        return f" La divicion de como resultado: {num1 / num2 / num3 / num4}"
    elif operation == "elevado":
        return f" La elevacion da como resultado: {num1 ** num2 **num3 **num4}"
    
if __name__  == '__main__':
    app.run(port = 5000 ,debug=True)