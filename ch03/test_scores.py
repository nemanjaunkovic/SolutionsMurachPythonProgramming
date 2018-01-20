#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()

while True:

    print("Enter test scores")
    print("Enter end to end input")
    print("======================")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0
    test_score_string = ""

    # loop for test scores for one test
    while True:
        test_score_string = input("Enter test score: ")
        if test_score_string.lower() == "end":
            break
        else:
            test_score = int(test_score_string)

        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        else:
            print("Test score must be from 0 through 100. Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the result
    print("======================")
    print("Total Score:", score_total,
          "\nAverage Score:", average_score)
    print()
    choice = input("Enter another set of test scores (y/n)? ")
    if(choice.lower() == "n"):
        break
    print()
    
print("Bye")


