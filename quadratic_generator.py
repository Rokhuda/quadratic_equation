import random

def generate_quadratic_equation_with_solution():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)
    discriminant = b**2 - 4*a*c
    while discriminant < 0 or a == 0:
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        discriminant = b**2 - 4*a*c
    equation = f"{a}x^2 + {b}x + {c}"
    solution = f"Step-by-step solution:\n"
    solution += f"Given equation: {equation}\n"
    solution += f"Discriminant (D) = b^2 - 4ac\n"
    solution += f"Substituting values: D = {b}^2 - 4*{a}*{c}\n"
    solution += f"Calculating discriminant: D = {discriminant}\n"
    solution += f"Since the discriminant is positive, the quadratic equation has real roots."
    return equation, solution

equation, solution = generate_quadratic_equation_with_solution()
print(equation)
print(solution)