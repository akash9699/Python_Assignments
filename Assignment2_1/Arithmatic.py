#Create one module named as Arithmatic which contains 4 functionsas 
#Add() for addition, Sub() for subtraction, Mult() For multiplication, Div() for Division.
# All function accepts two parameters as number and perform the operation.
# write python progrm which call all the functions from Arithmatic module by accepting the parameters from user


import Add
import Sub
import Mult
import Div

def main():
    No1= int(input("Enter No1: "))
    No2= int(input("Enter No2: "))

    res= Add.Addition(No1,No2)
    print(res)
    res= Sub.subtraction(No1,No2)
    print(res)
    res= Mult.Multiplication(No1,No2)
    print(res)
    res= Div.Division(No1,No2)
    print(res)

    

if __name__ == "__main__":
    main()
