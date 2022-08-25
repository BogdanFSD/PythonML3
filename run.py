#-----------------------------
import random


def start_game():
    """
    function that runs all necessary fnuction to start
    """
    attempts = []
    correct_attempts = 0
    question_num = 0 # index of questions to help me itarate 


    for question in questions:  #
        print("*" * 10) # just to make it more pleasant to for human eye
        print(question)
        for choice in choices[question_num]: # question_num helps me to print correct list of answer to specific question
            print(choice)                      # correct list of answer to specific question
        attempt = input("Choose an answer A, B, C or D:")
        attempt = attempt.upper() # so it is always uppercase 
        attempts.append(attempt)

        correct_attempts += correct_answers(questions.get(question), attempt)
        question_num += 1
    
    show_points(correct_attempts, attempts)

#-----------------------------
def correct_answers(answer, attempt):
    if answer == attempt:
        print("coorect")
        return 1
    else:
        print("wrong")
        return 0 
#-----------------------------
def show_points(correct_attempts, attempts):
    print("*" * 10)
    print("result")
    print("Answers: ")
    for i in questions:
        print(questions.get(i))
    print()

    print("Attempts")
    for i in attempts:
        print(i)
    print()

    score = int((correct_attempts/len(questions))*100)
    print("your score is " + str(score)+ "%")

    restart()
#-----------------------------
def restart():
    while True:
        response = input("Do you want to continue yes or no ")
        
        if response.lower() == "yes":
            print("great")
            start_game()
            return True

        elif response.lower() == "no":
            print("BYEEE")
            quit()

        else:
            print("Invalid entry. yes or no")
            
            
            continue

        
  
#-----------------------------

questions = {
    "Who open tesla?": "B",
    "Who discover America?": "C",
    "What shape our planet?": "D"
    
}

choices = [
    ["A. Musk", "B. huan", "C. Valera", "D. Dido"],
    ["A. vovo", "B. dfff", "C. Valera", "D. Dido"],
    ["A. asdf", "B. huan", "C. fdsa", "D. Dido"]
    
    ]


if __name__ == "__main__":
    start_game()





