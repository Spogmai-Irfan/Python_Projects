print("Python Calculator")
a= float(input("Enter first number: "))
b= float(input("Enter second number: "))

print("Addition:", a+ b)
print("Subtraction:", a- b)
print("Multiplication:", a * b)
print("Division:", a/ b)

print("**************")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divsion")
spogmai=(input("choose operation:"))
c=int(input("Enter first num:"))
d=int(input("enter second num:"))
if spogmai=="1":
    print("Result:",c+d)
elif spogmai=="2":
    print("Result:",c-d)
elif spogmai=="3":
    print("Result:",c*d)
elif spogmai=="4":
    print("Result:",c/d)
else:
    print("wrong choice")

print("&&&&&&&&&&&&&&&&&&&&&&&")
def add(i,j):
    return i+j
def sub(i,j):
    return i-j
def  mult(i,j):
    return i*j
def division(i,j):
    return i/j
i=float(input("enter 1st num:"))
j=float(input("eneter  2nd num:"))
print("Addition:")
print("mult:")
print("sub:")
print("divi:")
spog=input("operation:")
if spog=="A":
    print("R:",add(i,j))
elif spog=="B":
    print("R:",sub(i,j))
elif spog=="C":
    print("R:",mult(i,j))
elif spog=="D":
    print("R:",division(i,j))
else:
    print("wrooooong Answer")

print("||||||||||||||||||")
import math
def power(q,w):
  return power(q**w)
def squareroot(q):
  return math.sqrt(a)
def module(q,w):
  return q%w
def percentage(q,w):
  return(q/w)*100
while True:

    print("\\\\\\\\\\\\")
    print("1. power")
    print("2. Squreroot")
    print("3. Module")
    print("4.pecentage")
    print("5. Exit")

    Talhooo = input("Choose: ")

    if Talhooo == "5":
        print("Goodbye!")
        break

    q = float(input("Enter first number: "))
    w= float(input("Enter second number: "))

    if Talhooo == "1":
        print("Result:", q**w)

    elif Talhooo == "2":
        print("Result:", math.sqrt(q))

    elif Talhooo == "3":
        print("Result:", q%w)

    elif Talhooo== "4":
        print("Result:", (q/w)*100)

    else:
        print("hellllo")
