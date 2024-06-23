print("\n\n\n-- INTERACTIVE TERMINAL v0.0.1 --")
print("Input some text, and the terminal will respond with a answer if the statement/question is valid.")
print("This means to write with correct grammar and punctuation.")
print("When a number is asked to be typed, type only a number, and it has to be an integer, and can not contain anything other than a number.")
print('Type "QUIT" to end the program.\n')
while 1 == 1: 
    message = input("Type something! >>   ")
    if message == "QUIT":
        break
    elif message == "Hello!":
        print("\nHi!\n")
    elif message == "Hello.":
        print("\nUh.. hello.\n")
    elif message == "Hello?":
        print('\nWhy did you put a "?" at the end? Anyways, hello!\n')
    elif message == "What are you?":
        print("\nI am a terminal, but you can talk to me and I'll give you an answer.\n")
    elif message == "Who are you?":
        print("\nI am a computer program, not an actual person, but you can talk to me and I'll give you an answer.\n")
    elif message == "Ask me something!":
        age = input("\n    What's your age? >>   ")
        age = int(age)
        print(f"\n    So you're {age} years old! Cool!\n")
    elif message == "Ask me something.":
        age = input("\n    What's your age? >>   ")
        age = int(age)
        print(f"\n    So you're {age} years old! Cool!\n")
    elif message == "Tell me about my favorite number!":
        fav_num = input("\n    What's your favorite number? >>   ")
        fav_num = int(fav_num)
        if fav_num % 2 == 0:
            print(f"\n    Your number ({fav_num}) is even.\n")
        else:
            print(f"\n    Your number ({fav_num}) is odd.\n")
    elif message == "Tell me about my favorite number.":
        fav_num = input("\n    What's your favorite number? >>   ")
        fav_num = int(fav_num)
        if fav_num % 2 == 0:
            print(f"\n    Your number ({fav_num}) is even.\n")
        else:
            print(f"\n    Your number ({fav_num}) is odd.\n")
    elif message == "Do a math question!":
        number_1 = input("\n    Write the number that will be multiplied: >>   ")
        number_1 = int(number_1)
        number_2 = input("\n    Write the number that will be multiplying: >>   ")
        number_2 = int(number_2)
        print(f"\n    {number_1} multiplied by {number_2} is {number_1 * number_2}.\n")
    elif message == "Do a math question.":
        number_1 = input("\n    Write the number that will be multiplied: >>   ")
        number_1 = int(number_1)
        number_2 = input("\n    Write the number that will be multiplying: >>   ")
        number_2 = int(number_2)
        print(f"\n    {number_1} multiplied by {number_2} is {number_1 * number_2}.\n")
    else:
        print("\nSorry, I don't understand that. Make sure you're using correct grammar.\n")

print("\nProgram quit.\n\n\n")
