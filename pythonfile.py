import getpass

def add(num1, num2):
    return num1 + num2

def main():
    num1 = 3
    num2 = 5
    print(f"Hello {getpass.getuser()}")
    print(f"{num1} + {num2} = {add(num1, num2)}")

if __name__ == '__main__':
    main()