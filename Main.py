import math
# I am enabling myself to use math
# Lance Miller
# This is a combination of our programming exercises and code
# that was demonstrated in our resources
# My dad is going to be helping me when I require assistance
print("Hello!")
# I printed a greeting for the user
name = input("What is your name? ")
# I required the user to input something here
print("Welcome to my project,", name + "!")
# I used a string operator here to concatenate the users response with what
# I printed
print(
    "In this project, I will be displaying the knowledge that I gain "
    "throughout this course.")
# I explained what this program is going to do to the user
favNum = input(
    "What is your favorite whole number that is greater than 1 and less than "
    "100? ")
# I require another input from the user here
print(
    "Let's do some calculations using your favorite whole number that is "
    "greater than 1, which is",
    favNum + ".")
# Here I used the same string operator as before
print("The number you chose when added to the number five is:",
      int(favNum) + 5)
# Here I used a numeric operator to perform addition
print("The number you chose when subtracted from 100 is:", 100 - int(favNum))
# Here I used a numeric operator to perform subtraction
print("The number you chose raised to the 10th power is:", int(favNum) ** 10)
# Here I used a numeric operator to raise something to a power
print("The remainder that is left over when this number is divided by 2 is:",
      int(favNum) % 2)
# Here I used a numeric operator to find a remainder
print("That was fun! Let's do some more math with a different number.")
# I printed something here
numTwo = input("This time, pick any whole number from 100 - 1000. ")
# I require an input from the user here
print("Ah, I see that you have picked the number", numTwo + ".")
# Here I kind of converse with the user
print("This number divided by 10 is:", int(numTwo) / 10)
# Here I used a numeric operator to perform division
print("This number multiplied by 100 gives the number:", int(numTwo) * 100)
# Here I used a numeric operator to perform multiplication
print(
    "When we perform floor division on this number using the number 20, "
    "it results in:",
    int(numTwo) // 20)
# Here I used a numeric operator to perform floor division
print(
    "In case you do not know, floor division is similar to regular division, "
    "but it will result in the largest possible whole number")
# Here I explain floor division
print("Time for a surprise!")
# Here I print something for the user to see
wordChoice = input("For the first part, pick a random word, any word at all. ")
# Here I require an input from a user
print("I see you picked", wordChoice + " as your random word, nice choice!")
# Here I kind of converse with the user
print(
    "For the second part of you surprise, I am once again going to ask you "
    "to pick a number, and you can pick any number at all this time")
# Here I print something for the user to see
print(
    "Please do not pick too big of a number though, it might make my "
    "surprise less enjoyable.")
# Here I print something for the user to see
randomNum = input(
    "After careful consideration, what is the number that you have chosen? ")
# Here I require an input from the user
print("Thank you for participating")
# Here I kind of converse with the user
supAsking = input("Are you ready for the surprise? ")
# Here I require an input from the user
print("Either way, I will continue!")
# Here I print something for the user to see
print(wordChoice * int(randomNum))
# Here my surprise the user with my surprise, by using a string operator to
# print something multiple times
print("Surprise! I bet you were not expecting that")
# Here I print something for the user to see
print(
    "Anyway, enough with the games, there are some more things that I must "
    "show you.")
# Here I print something for the user to see
carnFood = input(
    "If you were able to go to a carnival right this instant, what food "
    "would you buy? ")
# Here I require an input from the user
carnNum = int(input("How many orders of that food would you buy? "))
# Here I require an input from the user and I make it an integer
carnCost = float(input(
    "Since I do not know, how much does one order of your chosen food cost? "
    "(Do not worry about the dollar sign) "))
# Here I require an input from the user and I make it a float
print("Thank you for all that information, I know it was a lot.")
# Here I print something for the user to see
carnTotal = carnNum * carnCost
# Here I use a numeric operator to find the carnTotal
print("Just to confirm with you, this is what I have")
# Here I print something for the user to see
print("Chosen Food: ", carnFood)
# Here I print something for the user to see
print("Number of orders you would like: ", carnNum)
# Here I print something for the user to see
print("Cost of one order: $", carnCost)
# Here I print something for the user to see
carnAsking = input("Is this correct? ")
# Here I require an input from the user
print(
    "I do not know what you are expecting, but I am going to continue "
    "regardless lol")
# Here I print something for the user to see
print("The total cost of your purchase is... drum roll please.")
# Here I print something for the user to see
print("Your total cost is ", format(carnTotal, ".02"), sep='$', end=' !')
# Here I use a sep= and end= argument to show a total cost
carnivalAsking = input("\nWas I right? ")
# Here I require an input from the user
print("Who am I kidding, I know I am right!")
# Here I print something for the user to see
print(
    "Do you remember how earlier I asked you to pick any whole number from "
    "100 - 1000? You picked",
    numTwo + ".")
# Here I print something for the user to see
print("Well I am going to do one more thing with that number.")
# Here I print something for the user to see
carnTwo = carnCost * int(numTwo)
# Here I use a numeric operator to find the carnTwo
print("If you were to buy ", numTwo + " orders of that carnival food, "
                                      "it would cost $",
      format(carnTwo, ".02f"), sep='')
# Here I use a sep= argument to show a total cost


print("For this next part, I am going to ask you for a number.")
# I am addressing the user
print(
    "It does not matter what number you pick, but maybe avoid picking a "
    "large number.")
# I am addressing the user
height = int(input("What is your number? "))
# I ask the user for an input
for i in range(1, height + 1):
    # I use "for", "in" and "range" functions
    for j in range(1, height - i + 2):
        # I use "for", "in" and "range" functions
        print(str(j) + " ", end='')
    # I print something for the user
    print()
# I have a print statement
print("Neat, right?")
# I am addressing the user

print(
    "Now, I will take a number you give me and set that as the radius of a "
    "circle.")
# I am addressing the user
print("I will then calculate the circumference of the circle you created.")


# I am addressing the user


def calculatecircumference(radius):
    # I am defining calculatecircumference
    circumference = math.pi * radius * 2
    # This is the formula for calculating circumference
    print("Your circumference is " + format(circumference, ".2f"))
    # Here I print what the users circumference is


def main():
    # I am defining main
    radius = int(input("What number do you pick? "))
    # I am passing to radius, and asking the user for an input
    calculatecircumference(radius)


# I call back to calculatecircumference(radius)

main()
# I call back to main()

print("I will now calculate the average of some numbers you give me.")
# I am addressing the user
print(
    "When you are done inputting numbers, enter the number 0, as that will "
    "let me know that you are done!")
# I am addressing the user
print(
    "Do not worry, 0 will not be included in your list of numbers when I "
    "calculate the average of the list.")
# I am addressing the user
value = int(input("Please enter a number: "))
# I am asking the user for an input
sum1 = 0
# I am setting a variable equal to zero
count = 0
# I am setting a variable equal to zero
while value != 0:
    # I use a while loop for when the value is not equal to zero
    sum1 += value
    # I am increasing a variable by whatever the user input
    count += 1
    # I use a shortcut operator here, and I increase an existing variable by
    # one
    value = int(input("Please enter a number: "))
# I am asking the user for an input
print("The average of this list of numbers is " + str(sum1 / count))
# I print the average of the users list of numbers

print("Let's see if you can guess my favorite color.")
# I am addressing the user
favColor = input("What is your guess? ")
# I ask the user for an input
if favColor == "blue":
    # I create an if statement for what to do when the input is blue
    print("Correct!")
# I print something for the user
elif favColor == "Blue":
    # I create an elif for when the input is Blue
    print("Correct!")
# I print something for the user
else:
    # I create an else for when the user does not input either of the
    # correct answers
    print("Incorrect, my favorite color is blue.")
# I print something for the user

coolNum = int(input("Give me a random number. "))
# I am asking the user for an input

if 0 <= coolNum <= 10:
    # I create an if for when two certain conditions are met by using "and"
    # and some operators
    print(
        "The number you gave me is in between 0 and 10, or is equal to 0 or "
        "10.")
# I display something to the user
elif coolNum < 0 or coolNum > 10:
    # I create an elif for when one of two conditions are met by using "or"
    # and some operators
    print("Your number is either less than zero or greater than 10.")
# I display something for the user


ageGuess = input("Guess my age. ")
# I ask the user for an input
if ageGuess == "18":
    # I create an if for when the user inputs 18, which is the correct answer
    print("Correct!")
# I display something for the user
else:
    # I create an else for when the correct answer is not the users input
    print("Incorrect, I'm actually 18.")
# I display something for the user

q = input("Either hit enter or type something random first ")
# I ask the user for an input
if not q:
    # I create an if for when something is not true by using "not"
    print("I see you chose to not enter anything.")
# I print something for the user
print("Thank you!")
# I print a message for the user
