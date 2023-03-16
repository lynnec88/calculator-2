"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod,)


# Replace this with your code

while True:
    user_input = input("Enter your equation:")
    tokens = user_input.split(' ')
    if "q" in tokens:
        print("you will quit the game")
        break
    elif len(tokens) < 2:
        print("too less")
        continue

    run = tokens[0]
    num1 = tokens[1]
    if len(tokens) < 3:
        num2 = "0"
    else:
        num2 = tokens[2]
        
    if len(tokens) > 3:
        num3 = tokens[3]

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("not numbers...")
        continue

    elif run == '+':
        result = add(float(num1),float(num2))
    elif run == '-':
        result = subtract(float(num1),float(num2))
    elif run == '*':
        result = multiply(float(num1),float(num2))
    elif run == '/':
        result = divide(float(num1),float(num2))
    elif run == 'square':
        result = square(float(num1)) 
    elif run ==  'cube':
        result = cube(float(num1))
    elif run == 'pow':
        result = power(float(num1),float(num2))
    elif run == 'mod':
        result == mod(float(num1),float(num2))
  
    else:
        result = "please enter something."

    print(result)
        




