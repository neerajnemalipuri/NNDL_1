#Delete 'h' and 'o' and reverse a string.
def reverse(string):
    string = string.replace('h','')
    string = string.replace('o','')
    rev = string[::-1]
    return rev

#Take input from the user and assign it to a variable
a = input("Enter a word: ")


print(a)

#calling reverse function 
print(reverse(a))

print("--------------------------")

#taking input, casting into int and assigning to two different variables
b = int(input("Enter first number: "))
c = int(input("Enter second number: "))

#Addition
add = b+c
#Subtraction
sub = b-c
#Multiplication
mul = b*c
#Division
div = b/c

#print statements
print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiplication: ",mul)
print("Division: ",div)

