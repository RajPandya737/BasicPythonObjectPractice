from Stack import Stack
from QuestionClass import Problem

def main():
    s = Stack()
    questions = ["How many colours are in a rainbow?", 
                "How many stars are in the American flag?", 
                "What is the most spoken language in the world?", 
                "What is the most common last name in England?"]
    answers = ["7", 
               "50", 
               "english", 
               "smith"]

    for i, v in enumerate(answers):
        q = Problem(questions[i], answers[i])
        s.push(q)
    score = 0
    for i in range(s.size()):
        q = s.pop()
        print(q.get_question())
        ans = input()
        if ans.lower().strip() == q.get_answer():
            print("correct")
            score+=1
        else:
            print("Incorrect")
    print(f"You scored {score}/4. Thank you for playing")



if __name__ == "__main__":
    main()
