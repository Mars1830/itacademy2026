def main():
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()


def task1():
    fullname = input("Enter your full name: ")
    name_lst = fullname.split(" ")
    last_name = name_lst[0]
    first_name = name_lst[1]
    patronym = name_lst[2]
    print(f"Your name: {last_name} {first_name[0]}. {patronym[0]}.")

def task2():
    str = input("Enter a string containing a few words: ")
    print(f"Number of words in the string: {len(str.split(" "))}")


def task3():
    str = input("Enter a string: ")
    print(f"Reversed string: {str[::-1]}")


def task4():
    str = input("Enter a string containing a few words: ")
    new_str = str.replace(" ", "")
    print(f"New string: {new_str}")


def task5():
    str = input("Enter a string: ")
    sub_str = input("Enter a string to find: ")
    print(f"Is sub string in string: {sub_str in str}")


def task6():
    str = input("Enter a string: ")
    old_symbol = input("Enter a symbol to find: ")
    new_symbol = input("Enter new symbol: ")
    new_str = str.replace(old_symbol, new_symbol)
    print(f"New string: {new_str}")


def task7():
    str = input("Enter a string: ")
    print(f"Is the string a number: {str.isdigit()}")


main()