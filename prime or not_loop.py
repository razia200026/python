n = int(input("Enter number : "))

if n <= 1:
    print("Number is not prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
