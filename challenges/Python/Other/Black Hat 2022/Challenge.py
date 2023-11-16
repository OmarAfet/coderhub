def String_Equation(equation: str):
    
    solution = equation.split(" ")
    
    nums = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9}
    
    part1 = ""
    part3 = ""
    
    if solution[0] in nums:
        part1 = nums[solution[0]]

    if solution[2] in nums:
        part3 = nums[solution[2]]

    if solution[1] == "Plus":
        solution = part1 + part3
    elif solution[1] == "Minus":
        solution = part1 - part3
    elif solution[1] == "Multiply":
        solution = part1 * part3
    elif solution[1] == "Divide":
        try:
            solution = part1 / part3
        except ZeroDivisionError:
            return "Undefined"
        
    solution = str(solution)
    solution = list(solution)
        
    Reverse_nums = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
    
    negative = False
    num1 = ""
    num2 = ""
    
    if solution[0] == "-":
        negative = True
    
    if len(solution) > 0 and solution[0] in Reverse_nums:
        num1 = Reverse_nums[solution[0]]
    
    if len(solution) > 1 and solution[1] in Reverse_nums:
        num2 = Reverse_nums[solution[1]]
    
    
    solution = f"{num1} {num2}"

    if negative:
        solution = f"Minus{num1} {num2}"
    
    return solution
