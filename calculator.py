def calc(a, b, ops):
    if ops not in "+*-/":
        return "error"
    if ops == "+":
        return str(a) + " " + ops + " " + str(b) + " = " + str(a + b)
    elif ops == "-":
        return str(a) + " " + ops + " " + str(b) + " = " + str(a - b)
    elif ops == "*":
        return str(a) + " " + ops + " " + str(b) + " = " + str(a * b)
    elif ops == "/":
        if b == 0:
            return "Sıfıra bölmek olmaz!"
        return str(a) + " " + ops + " " + str(b) + " = " + str(a / b)
while True:
    x = int(input('Please first number: '))
    y = int(input('Please second number: '))
    ops = input("Please choose one: +, -, *, /: ")
    print(calc(x, y, ops))
