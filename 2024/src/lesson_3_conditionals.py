print("Hello there!")

name = input("What is your name? ")
age = input("How old are you? ")

age = int(age)

print("Hello " + name + "! You are " + str(age) + " years old.")

if age < 21:
    print("You can not drink legally.")
else:
    print("You can drink legally!")
    
answer = input("Do you want to play a math game? (yes or no) ")

if answer == "no":
    print("Goodbye!")
elif answer == "yes":
    print("Ok!")
    number = int(input("What is 2 + 2? "))
    
    if number == 4:
        print("Correct!")
    else:
        print("Wrong! The answer is 4.")
else:
    print("You did not answer my question correctly! Bye!")