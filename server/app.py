from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<parameter>")
def print_string(parameter):
    return parameter


@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = "\n".join(map(str, range(parameter + 1)))
    return numbers


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    elif operation == "modulo":
        if num2 == 0:
            return "Modulo by zero is not allowed."
        result = num1 % num2
    else:
        return "Invalid operation"

    return str(result)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
