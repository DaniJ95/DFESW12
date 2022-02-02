#1. Write a Python function to find the Max of three numbers.

#var1 = int(input("number 1"))
#var2 = int(input("number2"))
#var3 = int(input("number3"))

#def largest_number(a, b, c):
#    if a > b and a > c: 
#        return a 
#    elif b > a and b > c:
#        return b
#    elif c > a and c > b:
#        return c
#    else: 
#        print("invalid input")
#
#print(largest_number(var1, var2, var3))

#2. Write a Python function to sum all the numbers in a list.

#list = [1,2,3,4,5]

#def sum(list):
#    total = 0
#    for item in list:
#        total = total + item
#    return total
#
#print(sum(list))

#3. Write a Python function to multiply all the numbers in a list.

#list = [1,2,3,4,5]

#def product(list):
#    total = 1
#    for item in list:
#        total = total * item 
#    return total

#print(product(list))

#4. Write a Python program to reverse a string.

#input = input("Insert a string to reverse:")

#def reverse(string):
#    reversed = ""
#    for count in range(len(string) -1, -1, -1):
#        reversed = reversed + string[count]
#    return reversed

#print(reverse(input))

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument

#x = int(input("enter a number"))

#def factorial(a):
#    total = 1
#    for count in range(a, 0, -1):
#        total = total * count
#    return total

#print(factorial(x))

#6. Write a Python function to check whether a number falls in a given range (50-100inc)

#x = int(input("insert number"))

#def CheckRange(a):
#    if a in range(50, 101):
#        return "is between 50 and 100"
#    else:
#        return "is not between 50 and 100"

#print(CheckRange(x))

# 7.  Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

#from curses.ascii import islower, isupper


#x = input("insert to find out how many UPPER and lower case letters there are: ")

#def NoCaps(a):
#    CapTotal = 0
#    NoCapTotal = 0
#    for item in a:
#        if item.isupper():
#            CapTotal +=1
#        else:
#            NoCapTotal +=1
#    return[CapTotal, NoCapTotal]

#print(NoCaps(x))

#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.

#x = [1,2,3,3,3,4,4,5,6,7,7,8,9,9,9,9,10]

#def unique_element(a):
#    uniquelist = []
#    for item in a:
#        if item not in uniquelist:
#            uniquelist.append(item)
#    return(uniquelist)
#
#print(unique_element(x))

#9. Write a Python function that takes a number as a parameter and check the number is prime or not.

#x = int(input("Insert number to check if prime"))

#def prime(x):
#    if (x==1):
#        return False
#    elif (x==2):
#        return True
#    else:
#        for y in range(2,x):
#            if(x % y==0):
#                return False
#        return True

#print(prime(x))

#10. Write a Python program to print the even numbers from a given list.

#x = [1,2,3,4,5,6,7,8,9,10]

#def listeven(a):
#    evenlist = []
#    for item in a:
#        if(item % 2==0):
#            evenlist.append(item)
#    return(evenlist)

#print(listeven(x))