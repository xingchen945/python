def collatz(number):
    print(number)
    if number == 1:
        return number
    else:
        if number % 2 == 0:
            collatz(number // 2)
        else:
            collatz(3 * number + 1)

if __name__ == "__main__":
    try:
        number = int(input("Enter a number："))
        result = collatz(number)  
    except:
        print("Enter a number!")
           