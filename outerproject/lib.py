def new_func():
    name = str(input("What is your name?"))

    if name.isalpha():
        return f"Hello, {name}! Hope you're doing well today!"
    else:
        name = input("Sorry, please provide your name in letters!")


if __name__ == "__main__":
    print("Function works")
