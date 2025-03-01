#Writing a python program to check if the user input number is even or odd:
number = int(input("Enter your number: \n")) #'\n' is used to introduce 'next line' inside a string.

if number%2 == 0:
    print(f"Given number {number} is Even")
    print(f"Given number '{number}' is Even") #Formatting can be used to print variable in between string.
    print(f"""Given number '{number}' is Even""")
    print(f'Given number "{number}" is Even')
    print(f'''Given number "{number}" is Even''')
    print(f'Given number \'{number}\' is Even') #This is scape sequence

else:
    print(f"Given number {number} is Odd")
    print(f"Given number '{number}' is Odd")
    print(f"Given number '''{number}''' is Odd""")
    print(f'Given number "{number}" is Odd')
    print(f'Given number """{number}""" is Odd''')
    print(f"Given number \"{number}\" is Odd")
#if-else is used for conditional statements.

#Note: Check on scape sequences.





