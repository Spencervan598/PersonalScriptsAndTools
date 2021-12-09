#creating functions
def Add():
    FNum = (input("First Number: "))
    SNum = (input("Second Number: "))
    print (float(FNum) + float(SNum))
def Subtract():
    FNum = (input("First Number: "))
    SNum = (input("Second Number: "))
    print (float(FNum) - float(SNum))
def Multiply():
    FNum = (input("First Number: "))
    SNum = (input("Second Number: "))
    print (float(FNum) * float(SNum))
def Divide():
    FNum = (input("First Number: "))
    SNum = (input("Second Number: "))
    if int(SNum) == 0:
        print ("Cannot Divide by Zero")
    else:
        print (float(FNum) / float(SNum))
print ("Simple Calculator \nDo not divide by zero!")
done = 'n'

while str(done) != 'y' or 'Y':
    Op = input("What Operation(+ - / *)? ")
    if Op == "+":
        Add()
    elif Op == "-":
        Subtract()
    elif Op == "/":
        Divide()
    elif Op == "*":
        Multiply()
    elif Op == "quit":
        break
    else:
        print("Incorrect Operator")
    done = input("Done? (y)es or (n)o: ")
 