def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()


def task1():
    name = input("Enter your name: ")
    print(type(name))


def task2():
    number = input("Enter a number: ")
    number_int = int(number)
    print(f"Your number: {number_int}, ", f"type: {type(number_int)}")


def task3():
    number = input("Enter a fractional number: ")
    number_float = float(number)
    print(f"Your number: {number_float}, ", f"type: {type(number_float)}")


def task4():
    first_number = input("Enter the first number: ")
    first_number_int = int(first_number)
    second_number = input("Enter the second number: ")
    second_number_int = int(second_number)
    numbers_sum = first_number_int + second_number_int
    print(f"Sum: {numbers_sum}")


def task5():
    str = input("Enter a string containing a few words: ")
    lst = str.split(" ")
    print(f"List: {lst}, ", f"type: {type(lst)}")


def task6():
    str = input("Enter a string: ")
    print(f"String length: {len(str)}")


def task7():
    str = input("Enter anything: ")
    str_bool = bool(str)
    print(f"Bool: {str_bool}")


def task8():
    first_str = input("Enter the first string: ")
    second_str = input("Enter the second string: ")
    new_str = first_str + " " + second_str
    print(f"New string: {new_str}")


def task9():
    str = input("Enter a string: ")
    index = int(input("Enter the index: "))
    symbol = str[index]
    print(f"str[index] = {symbol}")


def task10():
    str = input("Enter a string: ")
    print(f"Is the string a number: {str.isdigit()}")

main()