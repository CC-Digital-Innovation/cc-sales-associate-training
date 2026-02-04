import random

def play_math_game():
    print("Ok!")
    
    random_number_1 = random.randint(1, 9)
    random_number_2 = random.randint(1, 9)
    correct_answer = random_number_1 + random_number_2
    
    user_answer = int(input("What is " + str(random_number_1) + " + " + str(random_number_2) + "? "))
    
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Wrong! The answer is " + str(correct_answer))

print("Hello there!")

name = input("What is your name? ")
age = input("How old are you? ")

age = int(age)

print("Hello " + name + "! You are " + str(age) + " years old.")

if age < 21:
    print("You can not drink legally.")
else:
    print("You can drink legally!")

answer = "yes"

while answer == "yes":
    answer = input("Do you want to play a math game? (yes or no) ")

    if answer == "no":
        print("Goodbye!")
    elif answer == "yes":
        play_math_game()
    else:
        print("You did not answer my question correctly! Bye!")