def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations_dict = {
    "1": ("+", add),
    "2": ("*", multiply),
    "3": ("/", divide),
    "4": ("-", subtract)
}

def my_calculator():
    num_1 = float(input("Please enter the first number: "))
    
    print("Select operation:")
    print("1: Addition (+)")
    print("2: Multiplication (*)")
    print("3: Division (/)")
    print("4: Subtraction (-)")

    continue_flag = True
    while continue_flag:
        choice = input("Pick an operation (1/2/3/4): ")
        if choice in operations_dict:
            operation_symbol, calculator_function = operations_dict[choice]
            num_2 = float(input("Please enter the next number: "))
            calculation_output = calculator_function(num_1, num_2)
            print(f"{num_1} {operation_symbol} {num_2} = {calculation_output}")

            calculation_continue = input(f"Enter 'yes' to continue calculation with {calculation_output}, 'n' to start a new calculation, or 'x' to exit: ").lower()
            if calculation_continue == 'yes':
                num_1 = calculation_output
            elif calculation_continue == 'n':
                continue_flag = False
                my_calculator()
            elif calculation_continue == 'x':
                continue_flag = False
            else:
                print("Invalid input, exiting the calculator.")
                continue_flag = False
        else:
            print("Invalid input, please select a valid operation.")

my_calculator()
