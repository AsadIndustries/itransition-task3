from flask import Flask, request

app = Flask(__name__)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

@app.route('/xudoyberganovasadbek60_gmail_com')
def compute():
    x = request.args.get('x')
    y = request.args.get('y')

    if not x or not y:
        return "NaN"

    if not x.isdigit() or not y.isdigit():
        return "NaN"

    x = int(x)
    y = int(y)

    return str(lcm(x, y))

if __name__ == '__main__':
    app.run()