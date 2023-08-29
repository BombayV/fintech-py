class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


previousAnswers = []


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(expression):
    if expression == "":
        return 0

    expression = expression.split(" ")
    if len(expression) < 3:
        return 0

    if expression[1] not in symbols:
        return 0

    previousNumbers = []
    currentResult = 0
    for i in range(len(expression)):
        if expression[i] == "+" or expression[i] == "-":
            print("add or subtract")
            previousNumbers.append(currentResult)
        else:
            print("multiply or divide")



while True:
    userInput = input(f"{colors.OKGREEN}Choose your option {colors.ENDC}(quit, history, expression): ")
    if userInput == "quit":
        exit(0)
    elif userInput == "history":
        if len(previousAnswers) == 0:
            print(f"{colors.FAIL}No history{colors.ENDC}")
            continue

        for idx in range(len(previousAnswers)):
            print(f"{colors.OKGREEN}{idx + 1}{colors.ENDC}) {colors.OKBLUE}{previousAnswers[idx]}{colors.ENDC}")
        continue
    elif userInput == "expression":
        userInput = input(f"{colors.OKGREEN}Enter an expression {colors.ENDC}(+, -, *, /): ")
        result = calculate(userInput)
        print(f"{colors.OKBLUE}{result}{colors.ENDC}")

        previousAnswers.append(result)
        if len(previousAnswers) > 10:
            previousAnswers.pop(0)
        continue
    else:
        print(f"{colors.FAIL}Invalid option{colors.ENDC}")
        continue
