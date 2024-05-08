# python algorithm

# switch two numbers using an algorithm without a third temporary number


def switchNumber(inputA, inputB):
    a = inputA
    b = inputB
    a += b
    b = a - b
    a -= b
    return f"Input A = {inputA}\nInput B = {inputB}\nAfter Algorithm:\nA = {a}\nB = {b}"
    
# switchNumber()
print(switchNumber(10, 5))
print(switchNumber(5, 25))