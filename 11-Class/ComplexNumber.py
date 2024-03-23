class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_part = self.real + other.real
        imag_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imag_part)

    def multiply(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imag_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imag_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# Examples
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 4)

# Addition
result_add = num1.add(num2)
print(f"Addition: {result_add}")

# Multiplication
result_mul = num1.multiply(num2)
print(f"Multiplication: {result_mul}")

# Subtraction
result_sub = num1.subtract(num2)
print(f"Subtraction: {result_sub}")