a = int(input("Enter your age"))

if(a>18):
    print("yes,you are above the age of consent")

elif(a<0):
    print("you are entering an invalid negative age")

elif(a==0):
    print("you are 0 which is not a valid age")

else:
    print("you are below the age of consent")

    