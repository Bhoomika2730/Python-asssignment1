#Lets Play With Fibonacci
#Write a Python program to get the Fibonacci series between 0 to 50

"Fibonacci series starts with 0,1...and the result of the next number would be the addition of the two previous numbers."
"let us consider two numbers 0 and 1"
num1 = 0
num2 = 1
for i in range(50):
    print(num1)
    next_num=num2+num1
    num1 = num2
    num2 = next_num