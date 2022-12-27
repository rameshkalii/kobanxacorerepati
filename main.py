# Kaun banega corore pati.
money = 100000
q1 = "Who is the prime minister of Nepal? : "
q2 = "Who is the president of Nepal? : "
q3 = "What is the area of nepal? : "
a1 = "puspa kamal dahal"
a2 = "bidhya devi bhandari"
a3 = "1,47,181" 

questions = [q1, q2, q3]
answers = [a1,a2, a3]
for i in range(3):
    answer = input(questions[i])
    answer = answer.lower()
    print(answer)
    if answer== answers[i]:
        money = 10* money
    else:
        money = 0
print("Your current money is "+ str(money))
if money!=0:
    print("Congratulation you are cororepati!!!")
    
