import math


class Calculator:
    def __init__(self):
        self.calculation = ""

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)

    def evaluate_calculation(self):
        try:
            self.calculation = str(eval(self.calculation))
        except:
            self.calculation = "Error"

    def clear_field(self):
        self.calculation = ""

    def perform_calculation(self):
        try:
            self.calculation = str(eval(self.calculation))
        except:
            self.calculation = "Error"

    def add(self):
        self.add_to_calculation("+")

    def subtract(self):
        self.add_to_calculation("-")

    def multiply(self):
        self.add_to_calculation("*")

    def divide(self):
        self.add_to_calculation("/")

    def square_root(self):
        try:
            result = math.sqrt(eval(self.calculation))
            self.calculation = str(result)
        except:
            self.calculation = "Error"

    def power_of_2(self):
        try:
            result = pow(eval(self.calculation), 2)
            self.calculation = str(result)
        except:
            self.calculation = "Error"

    def factorial(self):
        try:
            result = math.factorial(eval(self.calculation))
            self.calculation = str(result)
        except:
            self.calculation = "Error"
