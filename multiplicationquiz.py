#juliana
#multiplication quiz
import random





#functions

def multiplication_quiz():
    print("Hello and welcome to the randomly generated Multiplication Quiz")
    mode = input("Would you like to play normal mode(n) or endless mode(e)?")
    if mode == "n":
        ans = input("Please select a difficulty to play on: easy(e), medium(m), or hard(h)")
        if ans == "e":
            times = input("How many questions would you like to have on this quiz?")
            score = 0
            for i in range(int(times)):
                num1 = random.randint(1, 5)
                num2 = random.randint(1, 5)
                answer = num1 * num2
                ans = input(("""Question:
        What is """+str(num1)+""" x """+str(num2)+"""?"""))
                if int(ans) == answer:
                    print("""Your answer is: """+str(ans)+"""
        Correct!""")
                    score = score + 1
                else:
                    print("""Your answer is: """+str(ans)+"""
        Incorrect""")
                    score = score
            print("Your final score is "+str(score)+"/"+times)
        elif ans == "m":
            times = input("How many questions would you like to have on this quiz?")
            score = 0
            for i in range(str(times)):
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
                answer = num1 * num2
                ans = input(("""Question:
        What is """+str(num1)+""" x """+str(num2)+"""?"""))
                if int(ans) == answer:
                    print("""Your answer is: """+str(ans)+"""
        Correct!""")
                    score = score + 1
                else:
                    print("""Your answer is: """+str(ans)+"""
        Incorrect""")
                    score = score
            print("Your final score is "+str(score)+"/"+times)
        elif ans == "h":
            score = 0
            for i in range(str(times)):
                times = input("How many questions would you like to have on this quiz?")
                num1 = random.randint(1, 15)
                num2 = random.randint(1, 15)
                answer = num1 * num2
                ans = input(("""Question:
        What is """+str(num1)+""" x """+str(num2)+"""?"""))
                if int(ans) == answer:
                    print("""Your answer is: """+str(ans)+"""
        Correct!""")
                    score = score + 1
                else:
                    print("""Your answer is: """+str(ans)+"""
        Incorrect""")
                    score = score
            print("Your final score is "+str(score)+"/"+times)
    elif mode == "e":
        score = 0
        total = 0
        while True:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            answer = num1 * num2
            ans = input(("""Question:
        What is """+str(num1)+""" x """+str(num2)+"""?"""))
            if int(ans) == answer:
                print("""Your answer is: """+str(ans)+"""
        Correct!""")
                score = score + 1
                total = total + 1
                print("Your  score is "+str(score)+"/"+str(total))
            else:
                print("""Your answer is: """+str(ans)+"""
        Incorrect""")
                score = score
                total = total + 1
                print("Your  score is "+str(score)+"/"+str(total))






#main
multiplication_quiz()
