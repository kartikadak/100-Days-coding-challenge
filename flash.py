#!/usr/bin/python2

import random

flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest mammal?": "Blue whale",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the square root of 25?": "5",
    "What is the currency of Japan?": "Yen"
}

def quiz():
    print("Welcome to the Flashcard Quiz!")
    questions = flashcards.keys()
    questions = random.sample(questions,len(questions))
    score = 0
    for question in questions:
    	user_input = raw_input("{} \nWrite your answer: ".format(question)).strip().capitalize()
    	if user_input == flashcards[question]:
    		print("correct")
    		score +=1
    	else:
    		print("incorrect! the correct answer is :{}".format(flashcards[question]))
    print("Your score is {}/{}".format(score,len(questions)))
    
if __name__ == "__main__":
 	quiz()
