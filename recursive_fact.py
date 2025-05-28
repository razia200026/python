def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

#recursive sum
def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n
print(sum(4))
