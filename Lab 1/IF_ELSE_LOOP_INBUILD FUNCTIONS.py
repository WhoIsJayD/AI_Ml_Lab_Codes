# Conditional Statements
a = int(input("Enter variable a : "))
b = int(input("Enter variable b :"))
if a == b:
    print(f"{a} is equal to {b}.")
elif a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is less than {b}.")
else:
    print("Cannot Not be determined!")
# For Loop Example
temp_list = []
for i in range(100):
    temp_list.append(i)

# List Functions
print(f"Max Number : {max(temp_list)}")
print(f"Min Number : {min(temp_list)}")
print(f"Average Number : {sum(temp_list) / len(temp_list)}")
print(f"Sum of all numbers : {sum(temp_list)}")
print("Length of the list : ", len(temp_list))
print(f"Index of '10' in list : {temp_list.index(10)}")
print(f"Poping the last element of the list : {temp_list.pop()}")
print(f"Removing the first element of the list : {temp_list.pop(0)}")
print("Reversing the list : ", temp_list.reverse())
print("Sorting the list : ", temp_list.sort())

# String Functions
string = input("Enter a string : ")
print(string)
print("Upper Case :", string.upper())
print("Lower Case :", string.lower())
print("Capital Case : ", string.capitalize())
print("Title Case :", string.title())
print("Removes Spaces from string : ", string.strip())
print("Removes spaces from left side :", string.lstrip())
print("Removes spaces from right side :", string.rstrip())
print("Number of 'a' present in string :", string.count("a"))
print("Index of 'a' in string :", string.find("a"))
print("The String is alphanumeric or not ? ", string.isalnum())
print("The string is only alphabetical or not ?", string.isalpha())
print("The string is only numeric or not ?", string.isdigit())
print("The string is lower or not ?", string.islower())
print("The string is uppercase or not ?", string.isupper())
print("The string is a space or not?", string.isspace())
print("Max ", max(string))
print("Min ", min(string))
