


def add(num1,num2):
    return num1+num2

def substration(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

while True:
    print("#######")
    print("CAlculator")
    print("1: add")
    print("2: substract")
    print("3: multiplication")
    print("4: division")
    print("5: quite")

    option = input("select your operation : 1,2,3,4,5 ")

    if option =="5": 
        print("exiting proogram ...!")
        break
    if option in ('1','2','3','4'):
        num1=float(input("enter your frist number: "))
        num2=float(input("enter your second number: "))

        if option =="1":
            print('Result: ',add(num1, num2))

        elif option=="2":
            print("result: ",substration(num1,num2))
        elif option=="3":
            print("result: ",multiplication(num1, num2))
        elif option=="4":
            print("Result: ",div(num1,num2))
        else:
            print("invsalid options")