
# Creator: M7ilan
# https://profile.satr.codes/m7ilan/public/overview
# Discord: M7ilan#5185
# https://github.com/M7ilan

def postFix(expr: str) -> int:
    stack = []
    tokens = expr.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            right = stack.pop()
            left = stack.pop()
            result = 0
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            stack.append(result)
        else:
            stack.append(int(token))
    
    return stack[0]