from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    n = 11 
    result = arithmetic_progression(n)
    return f"Result: {result}"

# обчислює суму перших n членів арифметичної прогресії: Xn = 1, 5, 9 ...
def arithmetic_progression(n):
    if n < 0:
        raise Exception("Inapropriate input (try values bigger than '-1')")
    a1 = 1  # first term of progression
    d = 4   # step
    sum = n * (2*a1 + d*(n-1)) // 2
    return sum

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)