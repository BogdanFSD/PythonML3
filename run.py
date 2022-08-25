def greeting_screen():
    print("Welcome to a Fun Car Quiz! \nAre you ready to check your knowledge?")
    print("There are total of 4 question and 4 answers to each of them. Once you are done with all question you will receive your score.")
    

    while True:
        start = input("Are you ready for a rummmmmmble? (Yes/No) ")
        
        if start.lower() == "yes":
            print("great")
            start_game()
            return True

        elif start.lower() == "no":
            print("BYEEE")
            quit()

        else:
            print("Invalid entry. Yes or No")

            continue

    start_game()


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
        for choice in choices[question_num]: 
            print(choice) 
        
        while True:                    
            attempt = input("Choose an answer A, B, C or D: ").upper()
            if attempt in {"A", "B", "C", "D"}:
                attempts.append(attempt)
                break
            else:
                print("Invalid entry")

        correct_attempts += correct_answers(questions.get(question), attempt)
        question_num += 1
    
    show_points(correct_attempts, attempts)

#-----------------------------
def correct_answers(answer, attempt):
    if answer == attempt:
        print("corect")
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
        response = input("Do you want to continue? (Yes/No) ")
        
        if response.lower() == "yes":
            print("great")
            start_game()
            return True

        elif response.lower() == "no":
            print("BYEEE")
            quit()

        else:
            print("Invalid entry. Yes or No")

            continue

        
  
#-----------------------------

questions = {
    "Who Created tesla?": "A",
    "What does BMW stand for?": "C",
    "Which 2020 Audi model has the highest starting MSRP?": "D"
}

choices = [
    ["A. Elon Musk", "B. Bill Gates", "C. Ford", "D. Johny Depp"],
    ["A. Berlin Motor Works", "B. Brunswick Motor Works", "C. Bavarian Motor Works", "D. Borgoholzhausen Motor Works"],
    ["A. Q7", "B. S6", "C. TTS", "D. A8"]
    
    ]


if __name__ == "__main__":
    greeting_screen()





