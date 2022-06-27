# HardGuessNum

Updated version of an a past project

Instead of choosing whether to guess the computer's number, or have the computer guess yours...
    -Now you and the computer take turns guessing each other's number to see who can get it first. 

Instead of the written range always having 1-10000...
    -As you guess numbers the written range adjusts accordingly. 
        -i.e. The first guess is 7800. It's too low. The written range is now 7800-10000.'

Instead of the computer guessing randomly (which could result in over 10000 guesses!)...
    -The computer chooses half way between the range, elminating half the reamaining possibilities
    -For 1-10000 the computer will typically guess the number between 10-13 turns tops.

There is a commented out 'easy mode' where the computer guesses randomly as well
    *Make sure to comment out 'hard mode' if you uncomment 'easy mode'*
