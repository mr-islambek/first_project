def sum(value1, value2, operation):
    if operation == "*":
        return f"Result: { value1 * value2 }"

    if operation == "/":
        return f"Result: { int(value1 / value2) }"

    if operation == "-":
        return f"Result: { value1 - value2 }"

    if operation == "+":
        return f"Result: { value1 + value2 }"
    else:
        return f"Error!"


x1 = int(input("Enter first value: "))
x2 = int(input("Enter second value: "))
operation = input("Select operation (* / - +): ")

print(sum(x1, x2, operation))
