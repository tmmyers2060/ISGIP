# Taylor Myers
# Study guide/quiz game
# https://realpython.com/python-main-function/
# used this to figure out how to loop to the beginning
player_name = input("What is your name? \n :")


def main(player_name_count):
    """
    player_name_count
    """

    # use of != relational operator
    while player_name_count != 1:
        player_name_count += 1

        # the *3 after a string multiplies that string by 3
        # the + concatenates two strings without a space
        print("Hello, " * 3 + player_name + ".", end=' ')
        print("Welcome to ISGIP \n"
              "The Interactive Study Game in Progress! \n",
              end=' ')
        print(
            "This program is meant to be used as a study guide where you can \n"
            "interactively refresh your intro to computer science skills!")
        start = input("Are you ready? Yes or No \n :")
        # use of "or" boolean operator
        answer = 'Yes'
        answer2 = 'yes'
        # https://pythonexamples.org/python-if-else-example/
        # if/else pogil helped me figure out if/else statements
        # use of == operator
        if start == answer:
            print("Great! We will start with some multiple choice questions.")
        elif start == answer2:
            print("Great! We will start with some multiple choice questions.")
        else:
            print("That's okay, see you again next time!")
            main(player_name_count)

        # player answers a or b
        question = input("1. What is a string literal? \n(a)"
                         "A sequence of characters surrounded"
                         "by double quotations.\n"
                         "(b) A sequence of characters "
                         "NOT surrounded by double quotes. \n :")
        answer = 'a'
        score = 0
        score = int(score)
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was a")

        # moving onto next question
        question = input("2. input() and print() are examples of what \n"
                         "(a) functions \n(b) prompts \n(c) variables \n : ")
        answer = 'a'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was a")

        question = input(
            "3. What does + do to two strings? \n"
            "(a) it puts a space between then \n"
            "(b) it concatenates them \n : ")
        answer = 'b'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was b")

        question = input("4. What are the three main boolean operators? \n"
                         "(a) when, is, and not \n"
                         "(b) and, there, and but \n"
                         "(c) and, or, and not \n:")
        answer = 'c'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was b")

        final_score1 = str(score)
        print("Your score in this section is", final_score1, "out of 4!")

        print("Next we will move onto some short answer math questions")
        # ** calculates powers
        question = input("5. What is 2 ** 3? \n : ")
        answer = '8'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("incorrect, remember ** calculates powers, so 2**3= 8")
        # *calculates multiplication
        question = input("6. What is 15 * 3? \n :")
        answer = '45'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("incorrect, * is used for multiplication, 15*3= 45")
        # /calculates division
        question = input("7. What is 10/2? \n : ")
        answer = '5'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("Incorrect, we use / for division, so 10/2= 5")
        # %calculates remainder
        question = input("8. What is 12%5? \n : ")
        answer = '2'
        if question == answer:
            score = score + 1
            print("correct!")
        else:
            print(
                "Incorrect, % gives us the remainder of a number divided by"
                " another number, 5 goes into 12 twice so 12%5= 2")
        # calculates floor division
        question = input("9. What is 16//5? \n : ")
        answer = '3'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print(
                "Incorrect, we use // for floor division, floor division "
                "provides only the integer when diving two numbers "
                "and gets rid of the float at the end.")
        question = input("10. What is $10-$5? Type your answer "
                         "without a dollar sign \n : ")
        answer = '5'
        if question == answer:
            score += 1
            print("correct!")
        else:
            # the sep='' gets rid of the separation betweem the $ and 5
            # subtraction
            print("Incorrect, we use - for subtraction, "
                  "so $10-$5= $", answer, sep='')
        # + addition
        question = input("11. What is 5 + 5? \n : ")
        answer = '10'
        if question == answer:
            score += 1
            print("correct!")
        else:
            print("Incorrect, + is used for addition so 5+5= 10")

        print("We will now be going into some more complex questions")
        print("What would be the output to the following code?")
        question = input(
            "12. for x in range(5) \n     print(x, end=" ") \n: ")
        answer = '0 1 2 3 4'
        answer2 = '0, 1, 2, 3, 4'
        if question == answer:
            score += 1
            print("correct!")
        elif question == answer2:
            score += 1
            print(
                "you've got the right idea, just remember there would be no "
                "commas in between the numbers")
        else:
            print("incorrect, below is the correct answer")
            for x in range(5):
                print(x, end=" ")

        question = input(
            "13. If you were using the NOT operator in your answer what"
            " would you have to answer in order for 'True' to be returned? \n"
            "x = 5 \n"
            "y = 3 \n"
            "which is greater?: ")
        answer = 'not y'
        print(True or False, )
        if question == answer:
            score += 1
        else:
            print("To earn a point for this question you had to type 'not y'")

        # fixed score system, if/else is working good for questions so far
        final_score = str(score)
        if final_score > '4' and final_score < '14':
            print("\nGreat job! Your score in this section is " + final_score + " " +
                  "out of 13")
        else:
            print("\nYour score in this section is " + final_score + " " +
                  "out of 13")
        start_over = input("To try again type 'done': ")
        if start_over == 'done':
            main(player_name_count)
        elif start_over == 'Done':
            main(player_name_count)


main(player_name_count)

player_name_count = 0