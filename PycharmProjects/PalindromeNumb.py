# PALINDROME is nothing but any number or a string which remains unaltered even when reversed.
num = input("Enter a multiple of numbers: ")
num2 = num[::-1]
if num2 == num:
    print(num)
    print(num2)
    print("Palindrome")
else:
    print(num)
    print(num2)
    print("Not palindrome")


