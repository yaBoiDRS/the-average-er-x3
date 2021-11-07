import math

#average of 3 numbers
print("Welcome to the Average-er:")

#taking input to continuw
varcontinue = input("If you want to continue, smash | y |, else smash | n |: ")

if varcontinue == "y": #if statement usage
    print("Ok, Input your number: ")
else:
    print("wrong input, restart program!")
    exit() 

number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))

x = number_1 + number_2 + number_3 
fx = x/3

print("The average of these numbers is: " +str(fx))
print("Thank You!")

exit()
