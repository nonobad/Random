##checkpoint 8.1
##assume "name" references a string. write a loop that prints each character in the string.
#name = "Sydney"
#print(name[0])
#print(name[1])
#print(name[2])
#print(name[3])
#print(name[4])
#print(name[5])

#############################
##Code using the in operator to determine if 'd' is in my_string
#my_string = (input("input something"))
#if 'd' in my_string:
 #   print("D is in this string")
#else:
#    print("D isn't here")
#############################
##big references a string convert the string it references to lowercase and assign the 
##converted string to the variable "little"
#big = 'AAAA'
#little=big.lower()
#print(little)
#############################
##Write an if statement that displays 
##"digit" if the string references by the variable ch contains a numeric digit. otherwise, "no digit" should
##be displayed
#my_string = input("Enter something.")

#bruh = 'bruh69420'
#print(bruh.isalnum())
#returns true because it only contains letters and numbers
#bruh2= 'bruh69420@!'
#print(bruh2.isalnum())
#returns false because there are non-numeric and non-alphabetic characters
#bruhh = 'breh'
#print(bruhh.isalpha())
#returns true, all alphabetic characters
#bruh4 = '6189'
#print(bruh4.isalnum())
#returns true because there are only digits
#bro = 'BRUH'
#print(bro.islower())
#returns false because there are upper case characters
#brah = ' '
#print(brah.isspace())
#returns true, there are only whitespace characters
#BROH = 'BROH'
#print(BROH.isupper())
#returns true, all characters are uppercase
#------
#Alternatively, you can use if statements to determine what characters a string has. Ex: "if userstring.isdigit" and then use a statement to print out whether it is 
#------
#letters = 'abcd'
#print(letters, letters.upper())
#prints out the original string, then the upper-case version of the string. you can use .lower() to lowercase the string instead
#------
#jhj = '    Justine    '
#print(jhj.strip())
#This removes trailing and ending white spaces. strip.(char) removes all instances of whatever char you specificed
#------
#oh= input('Enter whatever: ')
#if oh.endswith('ah'):
#   print("ahaha")
#.endswith() checks for the chars within the brackets and returns 'true' if they're found.
#------
#Print nine rows increasing in length
#for count in range(1, 10):
#    print('8' * count)

#Print nine rows decreasing in length
#for count in range (8, 0, -1)
 #   print('8'* count)
#------
#date_string = '11/26/2020'
#date_list = date_string.split('/')
#print(date_list)
#You can use the split() argument to split up a string by using a char to signal a "split".
#print(f'Month: {date_list[0]}')
#print(f'day: {date_list[1]}')
#print(f'day: {date_list[2]}')
#You can use the format string function to look for "split" parts of a string.
#------

#Some strings have a series of words or other data separated by spaces-- these are called "tokens"; the spaces separating them are "delimiters"-- delimiters can be any character that a prorammer sets them to be.
#csv_file = open('departments.csv', 'r')
#lines = csv_file.readlines()
#for row in lines:
#    print(lines)
#csv_file.close()

#big = 'BRUH'
#little = big.lower()
#print(big)
#print(little)


#digitornodigit = input('enter a string')
#for ch in digitornodigit:
#    if ch.isdigit():
#        print("digit")
#    else:
#        print("No digit")
## This checks to see if there are digits in the string
#------
#var = '$'
#print(var.upper())

#------
#string = input("Type something in")
#count=0
#for ch in string:
#    if ch.isdigit():
#        count+=1
#print(count)
##This counts the digits in a string
#------
#string = input("Type a word")
#count = 0
#for ch in string:
#    if ch.isupper():
#        count+=1
#print(count)

#lopez = 'george'
#print(lopez.find('e'))

#mystr='yes'
#mystr+='no'
#mystr+='yes'
#print(mystr)

#mystr = 'abc' * 3
#print(mystr)
#mystring = 'abcdefg'
#print(mystring[2:5])

#numbers = [1, 2, 3, 4, 5, 6, 7]
#print(numbers[4:6])
#----
#why = input('berder\n')
#count = 0
#for ch in why:
#    if ch ==(' '):
#       count += 1
#print(count)
#count = 0
#countdigit = input('input something\n')
#for ch in countdigit:
#    if ch.isdigit():
#       count += 1
#print(count)
#------
#count = 0
#mystring = input('something\n')
#for ch in mystring:
#    if ch.islower():
#       count+=1
#print(count) 

#------
#def bruh():
#    mystring = input('type something in\n')
#    if mystring.endswith('.com'):
#        print('True')   
#    else:
#        print('false')
#bruh()
#remember that mystring will automatically index the length of the argument to the end of the string and check the chars for you
#-----
#mystring = "ttttttt"
#newstring = mystring.replace("t","T")
#print(newstring)
#------
#origstring = input()
#def reverse(origstring):
#    newstring = origstring[::-1] 
#    print(newstring)
#reverse(origstring)

#This reverses an inputted string
#----
#This is an example of slicing a string
#mystring = ('bruh')
#print(mystring[0:3])
#------
#mystring = ('schadenfreude')
#print(mystring[-3:])
#-----
#mystring = ('cookies>milk>fudge>cake>ice cream')
#-----
thing = input("type something in")
newthing = thing.replace(',','--...--')
print(newthing)
