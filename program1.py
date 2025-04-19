# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string


class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "addition" or self.operation == "+":
            return self.a + self.b
        elif self.operation == "subtraction" or self.operation == "-":
            return self.a - self.b
        elif self.operation == "multiplication" or self.operation == "*":
            return self.a * self.b
        elif self.operation == "division" or self.operation == "/":
            if self.b != 0:
                return self.a / self.b
        else:
            return "Invalid operation."

a = float(input("Enter operand a: "))
b = float(input("Enter operand b: "))
operation = input("Enter operation (Addition(+), Subtraction(-), Multiplication(*), Division(/)): ")


calc = Calculator(a, b, operation)

result = calc.calculate()

print(f"Result: {result}")