import random



easy_questions =["q1","q2","q3","q4","q5"]
easy_answers = ["a1","a2","a3","a4","a5"]


i = 4

for _ in range(0,20,1):
 n = random.randint(0,i)
 question1 = input(easy_questions[n])

 if question1 == easy_answers[n]:
    easy_questions.remove(easy_questions[n])
    easy_answers.remove(easy_answers[n])
    print(easy_questions)
    print("correct")

 else:
    print("wrong") 
    print(easy_questions)

 if i > 0: 
     i = i - 1

 if len(easy_questions) == 0:
     print("YOU HAVE COMPLETEED THE LIST")
     break    
  


print("worked")