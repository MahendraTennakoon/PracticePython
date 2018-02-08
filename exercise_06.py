user_input = input("Enter text: ")

reversed_input = user_input[-1::-1]

if user_input == reversed_input:
    print("Palindrome")
else:
    print("Not a palindrome")
