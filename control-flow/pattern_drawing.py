def draw_pattern():
    size = int(input("Enter the size of the pattern: "))
    i = 0
    
    while i < size:
        for j in range(size):
            print("*", end="")
        print()
        i += 1

if __name__ == "__main__":
    draw_pattern()