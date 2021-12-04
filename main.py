# Study guide/quiz game
# https://realpython.com/python-main-function/
# used this to figure out how to loop to the beginning
""" ISGIP """
__author__ = "Taylor Myers"


def main():
    """
    the main file this includes everything

    """
    import sys
    # i used this for the sys.exit() it allows me to end the program there

    # use of != relational operator
    player_name = input("What is your name? \n: ")
    player_name_count = 0
    scores = 0
    scores = int(scores)

    while player_name_count != 1:
        player_name_count += 1

        # the *3 after a string multiplies that string by 3
        # the + concatenates two strings without a space
        print("Hello, " * 3 + player_name + ".", end=' ')
        print("Welcome to ISGIP \n"
              "The Interactive Study Game in Progress!",
              end=' ')
        print(
            "\nThis program is meant to be used as a study guide\n"
            " where you can "
            "interactively refresh your intro to computer science skills!")
        start = input("Are you ready? Yes or No \n: ")
        # use of "or" boolean operator
        answer1 = 'Yes'
        answer2 = 'yes'
        # https://pythonexamples.org/python-if-else-example/
        # if/else pogil helped me figure out if/else statements
        # use of == operator
        if start == answer1:
            print("\nGreat! We will start with some multiple choice"
                  " questions.")
        elif start == answer2:
            print("\nGreat! We will start with some multiple choice"
                  " questions.")
        else:
            print("\nThat's okay, see you again next time!")
            sys.exit()
            # ends the program

        # player answers a or b
        question = input("\n1. What is a string literal? \n(a) "
                         "A sequence of characters surrounded"
                         "by double quotations.\n"
                         "(b) A sequence of characters "
                         "NOT surrounded by double quotes. \n: ")
        answer = 'a' or 'A'

        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was a")

        # moving onto next question
        question = input("\n2. input() and print() are examples of what \n"
                         "(a) functions \n(b) prompts \n(c) variables\n: ")
        answer = 'a' or 'A'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was a")

        question = input(
            "\n3. What does + do to two strings? \n"
            "(a) it puts a space between then \n"
            "(b) it concatenates them \n: ")
        answer = 'b' or 'B'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was b")

        question = input("\n4. What are the three main boolean operators? \n"
                         "(a) when, is, and not \n"
                         "(b) and, there, and but \n"
                         "(c) and, or, and not\n: ")
        answer = 'c' or 'C'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("incorrect, the correct answer was c")

        final_scores1 = str(scores)

        print("\nYour score in this section is", final_scores1, "out of 4!")

        print("Next we will move onto some short answer math questions,"
              "answers including numbers should be entered as whole numbers.")
        # ** calculates powers
        question = input("\n5. What is 2 ** 3? \n: ")
        answer = '8'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("incorrect, remember ** calculates powers, so 2**3 = 8")
        # *calculates multiplication
        question = input("\n6. What is 15 * 3? \n: ")
        answer = '45'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("incorrect, * is used for multiplication, 15*3 = 45")
        # /calculates division
        question = input("\n7. What is 10/2? \n: ")
        answer = '5'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("Incorrect, we use / for division, so 10/2 = 5")
        # %calculates remainder
        question = input("\n8. What is 12 % 5? \n: ")
        answer = '2'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print(
                "Incorrect, % gives us the remainder of a number divided by"
                " another number, 5 goes into 12 twice so 12 % 5 = 2")
        # calculates floor division
        question = input("\n9. What is 16//5? \n: ")
        answer = '3'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print(
                "Incorrect, we use // for floor division, floor division "
                "provides only the integer when diving two numbers "
                "and gets rid of the float at the end, so 16//5 = 3")
        question = input("\n10. What is $10-$5? Type your answer "
                         "without a dollar sign \n: ")
        answer = '5'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            # the sep='' gets rid of the separation between the $ and 5
            # subtraction
            print("Incorrect, we use - for subtraction, "
                  "so $10-$5= $", answer, sep='')
        # + addition
        question = input("\n11. What is 5 + 5? \n: ")
        answer = '10'
        if question == answer:
            scores += 1
            print("correct!")
        else:
            print("Incorrect, + is used for addition so 5+5 = 10")

        print("\nWe will now be going into some more complex questions")
        print("\nWhat would be the output to the following code?")
        question = input(
            "12. for x in range(5) \n     print(x, end=" ") \n: ")
        answer = '0 1 2 3 4'
        answer2 = '0, 1, 2, 3, 4'
        if question == answer:
            scores += 1
            print("correct!")
        elif question == answer2:
            print(
                "you've got the right idea, just remember there would be no "
                "commas in between the numbers")
        else:
            print("incorrect, below is the correct answer")
            for x in range(5):
                print(x, end=" ")

        question = input(
            "\n13. If you were using the NOT operator in your answer what"
            " would you have to answer in order for 'True' to be returned? \n"
            "x = 5 \n"
            "y = 3 \n"
            "which is greater?\n: ")
        answer = 'not y'
        print(True or False, )
        if question == answer:
            scores += 1
            print("Great job!")
        else:
            print("To earn a point for this question you had to type 'not y'")

        # fixed score system, if/else is working good for questions so far
        final_scores = str(scores)
        if '4' < final_scores < '14':
            print("\nGreat job! Your score in this section is "
                  + final_scores + " " +
                  "out of 13")
        else:
            print("\nYour score in this section is " + final_scores + " " +
                  "out of 13")
        start_over = input("To try again type 'done': ")
        if start_over == 'done':
            player_name_count = 0
        elif start_over == 'Done':
            player_name_count = 0
        else:
            print("Have a nice day!")


main()
if __name__ == "__main__":
    main()
