from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    n = 11 
    result = arithmetic_progression(n)
    return f"Result: {result}"

# обчислює суму перших n членів арифметичної прогресії: Xn = 2, 4, 6 ...
def arithmetic_progression(n):
    print("Ivanytska Anna")
    if n < 0:
        raise Exception("Inapropriate input (try values bigger than '-1')")
    a1 = 2  # first term of progression
    d = 2   # step
    sum = n * (2*a1 + d*(n-1)) // 2
    return sum

# обчислює суму перших n членів геометричної прогресії: 
def geometric_progression(n):
    if n < 0:
        raise Exception("Inapropriate input (try values bigger than '-1')")
    b1 = 2    # first term of progression
    q = 0.5   # denominator of the progression (знаменник)
    if q == 0:
        raise Exception("q can't be 0. Try other value")
    sum = b1 * (q**n - 1) / (q - 1)
    return sum

# рахує, скільки днів лишилося до дня народження. Формат вводу: yyyy-mm-dd
from datetime import datetime
def days_til_birthday(birthdate, today=None):
    if today is None:
        today = datetime.now()
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)  # date of birth in today year

    if today > next_birthday:   # comparing today date with date of birth in today year, if we already had birthday
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)   # se set a new year for our birthday

    days_left = (next_birthday - today).days  # counting days to our birthday 
    return days_left

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)