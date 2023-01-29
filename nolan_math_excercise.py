import numpy as np
import pandas as pd
from IPython.display import display
import datetime
import os

total_questions = 5
right_answer_count = 0
correct_rate = 0.8

all_questions_number_list = []
all_questions_list = []
all_right_answers_list = []
all_your_answer_list = []
right_or_wrong_list = []

print("Hi Mr. Nolan, let's kick off today's fun time for math Are you ready?! Let's go!!!!")
print("----------------------------------------------------------------------------------------")

print("We will randomly choose " +str(total_questions)+ " questions only on 3-digit addition or subtraction  ")
print("----------------------------------------------------------------------------------------")

print("Your goal is to be right on at least " + str(int(total_questions*correct_rate)) + " questions, lets GOOOOOOOO!!!! ")
print("----------------------------------------------------------------------------------------")


for num in np.arange(total_questions):
    print("question " + str(num+1) + ":")

    all_questions_number_list = all_questions_number_list + [num + 1]
    first_number  = np.random.randint(100,999)
    second_number = np.random.randint(100,999)

    sign_number = np.random.randint(-999, 999)

    if sign_number>0:
        calculation='addition'
    else:
        calculation='subtraction'

    if calculation=='addition':
        question = str(first_number) + "+" + str(second_number)
        all_questions_list = all_questions_list + [question]
        print("what's the result of " + question)
        answer = first_number + second_number
    elif calculation=='subtraction':
        if first_number > second_number:
            question = str(first_number) + "-" + str(second_number)
            all_questions_list = all_questions_list + [question]
            answer = first_number - second_number
            print("what's the result of " + question)
        else:
            question = str(second_number) + "-" + str(first_number)
            all_questions_list = all_questions_list + [question]
            answer = second_number - first_number
            print("what's the result of " + question)

    answer_from_nolan = input()
    #print("You have picked "+str(answer_from_nolan) +" as your answer")
    if int(answer_from_nolan) == answer:
        right_answer_count = right_answer_count+1
        right_or_wrong_list = right_or_wrong_list + ['right']
        print("Great, you are correct!")
    else:
        right_or_wrong_list = right_or_wrong_list + ['wrong']
        print("I am sorry, the right answer is " + str(answer))
    print("----------------------------------------------------------------------------------------")

    all_right_answers_list = all_right_answers_list + [answer]
    all_your_answer_list = all_your_answer_list + [answer_from_nolan]

print("You are getting " + str(right_answer_count) + " correct answers out of " + str(total_questions) +" questions")
if right_answer_count/total_questions>=0.8:
    if right_answer_count == total_questions:
        print("Phenominal Work !!! You got all the questions 100% correct !!!")
    else:
        print("Congrats, you have achieved your goal !!!")
else:
    print("Good luck next time ...")

print("----------------------------------------------------------------------------------------")
print("Let's review this exercise ...")
dict = {'Question_No.' : all_questions_number_list,
        'Question' : all_questions_list,
        'Your_Answer' : all_your_answer_list,
        'Right_Answer' : all_right_answers_list,
        'Right_or_Wrong' : right_or_wrong_list}
df = pd.DataFrame(dict)
df = df.set_index('Question_No.')
display(df)

print("Do you want to save your results today for future revisit? Hit 1 for yes ")
save_or_not = int(input())
if save_or_not==1:
    file_name = "Nolan_math_exercise_"  + str(right_answer_count) + "on" +str(total_questions) + "_" + datetime.datetime.now().strftime("%m-%d-%Y-%H-%M") + ".csv"
    df.to_csv(file_name)
    print("File succefully saved at " + os.path.join(os.getcwd(),file_name))

print("You might now hit anything to exit ...")
input()
