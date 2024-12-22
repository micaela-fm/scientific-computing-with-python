def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5: 
        return "Error: Too many problems."
        #raise ValueError("Too many problems.")
    
    first_line = ''
    second_line = ''
    dash_line = ''
    answer_line = ''
    blank_space = '    '

    for problem in problems: 
        first_operand, operator, second_operand = problem.split()

        if not (operator == '+' or operator == '-'):
            return "Error: Operator must be '+' or '-'."
            #raise ValueError("Operator must be '+' or '-'.")

        if not (first_operand.isdigit() and second_operand.isdigit()): 
            return "Error: Numbers must only contain digits."
            #raise ValueError("Numbers must only contain digits.")
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
            #raise ValueError("Numbers cannot be more than four digits")

        if show_answers:
            answer = str(eval(problem))

        max_len = max(len(first_operand), len(second_operand)) + 2
        first_line += first_operand.rjust(max_len) + blank_space
        second_line += operator + ' ' + second_operand.rjust(max_len - 2) + blank_space
        dash_line += '-' * max_len + blank_space
        if show_answers:
            answer_line += answer.rjust(max_len) + blank_space

        arranged_problems = f"{first_line}\n{second_line}\n{dash_line}"  

    if show_answers:
        arranged_problems += f"\n{answer_line}"
       
    problems = arranged_problems
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
