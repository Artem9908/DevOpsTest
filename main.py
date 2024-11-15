import itertools

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
operators = ['+', '-', '']  

for ops in itertools.product(operators, repeat=9):
    expression = ''.join(d + o for d, o in zip(digits, ops)) + digits[-1]
    try:
        if eval(expression) == 200:
            print(f"{expression} = 200")
    except Exception:
        continue
