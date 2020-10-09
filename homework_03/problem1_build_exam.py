#creating application to auto grade students answer
#base on giving correct answers

#requirement: read students answer file, compare it with correct answer
#then display a message contain:
#1. indication if student pass the test or not (minimum 15 correct answers to pass)
#2. total correct answer, incorrect answer
#3. list of incorrect answer
from tkinter.filedialog import askopenfilename
import traceback
import utils.get_input

#compare student answer to the correct answer and display message
def compare(students_answer,correct_answer):
    incorrect_answer = []

    #check if student_answer file is in correct format or not
    #correct format: 0 < number of lines <= 20
    if(len(students_answer) == 0 or len(students_answer) > len(correct_answer)):
        print('student_answer file is in incorrect format!')
        return

    for i in range (len(students_answer)):
        if(students_answer[i] != correct_answer[i]):
            incorrect_answer.append(students_answer[i])

    #check if student passed the test or not
    if(len(correct_answer) - len(incorrect_answer) >= 15):
        print('Student have passed the exam!')
    else:
        print('Student have failed the exam!')

    print(f"Correct answers: {len(correct_answer)- len(incorrect_answer)}")
    print(f'Incorrect answers: {len(incorrect_answer)}')
    print(f'Answer that are incorrect: {incorrect_answer}')

def main():
    cor_ans = utils.get_input.file_to_list("Enter correct answers path: ")
    stu_ans = utils.get_input.file_to_list("Enter student answers path: ")

    compare(cor_ans,stu_ans)

main()