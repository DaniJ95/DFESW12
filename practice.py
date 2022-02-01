#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

#nl=[]
#for x in range(1500, 2701):
 #   if (x%7==0) and (x%5==0):
 #       nl.append(str(x))
#print (','.join(nl))

#2 Write a Python program to convert temperatures to and from celsius, fahrenheit. 
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 

#temp = input ("Input the tempurature you would like to convert: ")
#degree = int(temp[:-1])
#i_convention = temp[-1]

#if i_convention.upper() == "C":
#	result = int(round((9 * degree) / 5 + 32))
#	o_convention = "fahrenhiet"
#elif i_convention.upper() =="F":
#	result = int(round((degree - 32)   /  9))
#	o_convention = "celsius"
#else:
#	print("input proper convention")
#	quit()
#print("The temperature in " + o_convention + " is " + str(result))

#3Write a Python program to guess a number between 1 to 9.

#import random
#target_num, guess_num = random.randint(1, 10), 0
#while target_num != guess_num:
#    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
#print('Well guessed!')

#4 Write a Python program to construct a pattern, using a nested for loop.

#for row in range(6):  
#    for col in range(7):  
#       if (row==0 and col %3 !=0)or(row==1 and col %3==0) or(row-col==2) or(row+col==8):  
#            print("*",end=" ")  
#        else:  
#            print(end=" ")  
#    print()  

#Write a Python program that accepts a word from the user and reverse it.

#word = input("Input a word to reverse: ")

#for char in range(len(word) - 1, -1, -1):
#  print(word[char], end="")
#print("\n")

#6. Write a Python program to count the number of even and odd numbers from a series of numbers.

#numbers = range (100) 
#count_odd = 0
#count_even = 0
#for x in numbers:
#       if not x % 2:
#    	     count_even+=1
#        else:
#    	     count_odd+=1
#print("Number of even numbers :",count_even)
#print("Number of odd numbers :",count_odd)

#7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

#datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
#{"class":'V', "section":'A'}]
#for item in datalist:
#   print ("Type of ",item, " is ", type(item))
   
#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement. 

#for x in range(6):
#    if (x == 3 or x==6):
#        continue
#    print(x,end=' ')
#print("\n")

#9. Write a Python program to get the Fibonacci series between 0 to 50. 

#x,y=0,1

#while y<50:
#    print(y)
#    x,y = y,x+y

#10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".



#for fizzbuzz in range(51):
#    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#        print("fizzbuzz")
#        continue
#    elif fizzbuzz % 3 == 0:
#        print("fizz")
#        continue
#    elif fizzbuzz % 5 == 0:
#        print("buzz")
#        continue
#    print(fizzbuzz)
