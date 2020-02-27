import random

#To welcome the user
def welcome():
    print('This is a math quiz program, GOOD LUCK!')
    print('It will continue until user enters a wrong answer')


#Choose a random mathematical operation
# Hint: use random.randint(a,b)    
def choosing_operation():
    #Your code starts here
    operation = random.randint(0,3)
    return operation
    #Your code ends here


#Compare the user answer and the correct answer, determine whether user answered correctly or not.
def compare_answers(answer, user):
    #Your code starts here
    result = False
    if(answer==user):
        result=True
    return result
    #Your code ends here


#Ask user until the answer is not correct with the numbers generated randomly.
#Again, use random.randint(a,b)
#Choose the mathematical operation every time by using choosing_operation function.
#Compare the user answer and the correct answer, determine whether it is true.
def questioning_part():
    #Your code starts here
    isCorrect = True
    correct_count=0
  
    while(isCorrect):
        x = random.randint(1,101)
        y = random.randint(1, 101)
        op = choosing_operation()
        if op==0:
            user=int(input(f'{x} + {y} = '))
            answer=x+y
           
        elif op==1:
            user=int(input(f'{x} - {y} = '))
            answer=x-y
            
        else:
            user=int(input(f'{x} * {y} = '))
            answer=x*y
            
        print(answer)
        isCorrect = compare_answers(answer, user)
        if isCorrect == True:
            correct_count+=1
    #Your code ends here
    print(f'Number of correct answers:  {correct_count}')

welcome()
questioning_part()