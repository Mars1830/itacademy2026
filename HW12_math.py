import math


# task 1
def circle_area(radius):
    area = math.pi * math.pow(radius, 2)
    return area


# task 2
def int_number(num):
    return math.floor(num)


# task 3
def sinus(degrees):
    return math.sin(math.radians(degrees))


# task 4
def square_root(num):
    return math.sqrt(num)


# task 5
def max_common_divisor(a, b):
    a_divisors = devisors(a)
    b_divisors = devisors(b)
    return max(a_divisors.intersection(b_divisors))


def devisors(num) -> set:
    num_devisors = set()
    for i in range(1, num):
        if num % i == 0:
            num_devisors.add(i)
    return num_devisors


# task 6
def e_pow(p):
    return math.exp(p)


# task 7
def fact(num):
    return math.factorial(num)


# task 8
def logarithm(power, base):
    return math.log(power, base)


# task 9
def num_round(num):
    if num % 1 < 0.5:
        return math.floor(num)
    else:
        return math.ceil(num)


# task 10
def tangent(degrees):
    return math.tan(math.radians(degrees))


if __name__ == '__main__':
    print(f"Circle area: {circle_area(7)}")
    print(f"Integer number: {int_number(9.8)}")
    print(f"Sinus 45: {sinus(45)}")
    print(f"Square root of 144: {square_root(144)}")
    print(f"Max common divisor in 270 and 192: {max_common_divisor(270, 192)}")
    print(f"e^3: {e_pow(3)}")
    print(f"Factorial of 8: {fact(8)}")
    print(f"Logarithm 256, base 2: {logarithm(256, 2)}")
    print(f"Num round: {num_round(3.14159)}")
    print(f"Tangent 60: {tangent(60)}")