def screen():
    print("-----Finding The Largest Number Among The Three Numbers-----")

def largestNumber(x,y,z):

    if (x >= y) and (x >= z):
        print("\nLargest number is {}.\n".format(x))
    elif (y >= x) and (num2 >= z):
        print("\nLargest number is {}.\n".format(y))
    else:
        print("\nLargest number is {}.\n".format(z))


while True:
    num1=int(input("First Number : "))
    num2=int(input("Second Number: "))
    num3=int(input("Thirt Number : "))

    largestNumber(num1, num2, num3)