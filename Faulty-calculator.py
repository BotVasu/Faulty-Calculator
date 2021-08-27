#Exercise - 2

operator  = input("Enter the operator you are using:")

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

if operator == "+":
    if (num1 == 56 and num2 == 9) or (num1 == 9 and num2 == 56):
        print("The addition is : 77")
    else:
        print("The addition is :", num1 + num2)
if operator == "-":
    print("The substration is : ", num1 - num2)
if operator == "*":
    if (num1 == 45 and num2 == 3) or (num1 == 3 and num2 == 45):
        print("The multiplication is : 555")
    else:
        print("The multiplication is :", num1 * num2)
if operator == "/":
    if (num1 == 56 and num2 == 6) or (num1 == 6 and num2 == 56):
        print("The division is : 4")
    else:
        print("The division is : ", num1 / num2)
