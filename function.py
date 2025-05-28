#function definition
def avg():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))

    average = (a + b + c) / 3
    print("Average:", average)

    avg()  # recursive call to repeat the function

avg()

#Add number
def add(x,y):
    sum = x+y
    print(sum)

add(10,20)  #function call
add(100,250)
