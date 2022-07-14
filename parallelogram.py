#This program will create a parallelogram after a user inputs how long they want #each side to be and what character they want it mae out of.
print("This program will output a parallelogram.\n")
#First, we get the user's desired length and what character they want the parallelogram to be made out of.
rows = int(input("How long do you want each side to be?"))
character = input("Please enter the character you want it to be made of.")

#Now, the program does its thing
for i in range(rows):
    print(" "*(rows+i)+character*(rows+1))


