def print_multiplication_table():
    number = int(input("Enter a number to see its multiplication table: "))
    
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

if __name__ == "__main__":
    print_multiplication_table()