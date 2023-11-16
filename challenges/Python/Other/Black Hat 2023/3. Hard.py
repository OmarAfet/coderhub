# Not sure about the function name

def is_brackets_balanced(s: str) -> bool:
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    stack = []

    for char in s:
        if char in bracket_pairs:
            stack.append(char)
        else:
            if not stack or bracket_pairs[stack.pop()] != char:
                return False

    return len(stack) == 0
