"""
Simple Quiz Game ❓
Ask multiple-choice or true/false questions.

Track score.

Randomize question order.
"""
import random

print("------------------------MATH QUIZ------------------------")
q_a = {}
ch1 = {
    "The empty set is a subset of every set." : "T",
    "The set of all vowels in the word 'MATH' is {A}." : "T",
    "The number of subsets of a set with 4 elements is 8." : "F",
    }
ch2 = {
    "A function can have two outputs for the same input." : "F",
    "The function f(x) = 3x + 1 is a one-one function." : "T",
    "The range of the constant function f(x) = 5 is {5}." : "T",
    "The domain of f(x) = √(x − 2) is all real numbers." : "F",
    "Every relation is a function." : "F",
}
ch3 = {
    "sin²x + cos²x = 1 for all real x" : "T",
    "tan x is defined for x = 90°." : "F",
    "cos(–x) = cos x." : "T",
    "sin(–x) = –sin x." : "T",
    "sec x is the reciprocal of sin x.": "F",
    "The range of sine function is [–1, 1].": "T",
    "The principal value of sin⁻¹(½) is π/6." : "T",
    "cos⁻¹(–1) = π." : "T"
}
ch4 = {
    "i² = 1." : "F",
    "The complex number 3 + 4i lies in the first quadrant." : "T",
    "A quadratic equation always has two real roots." : "F",
    "The roots of x² + 1 = 0 are imaginary." : "T",
    "If D < 0 in a quadratic equation, the roots are complex." : "T",
    "√–9 = 3i." : "T"
}
ch5 = {
        "An arithmetic progression (A.P.) has a common difference." : "T",
    "The nth term of an A.P. is given by a + (n – 1)d." : "T",
    "The sum of first n terms of a geometric progression (G.P.) is always finite." : "F",
    "In an A.P., if a = 2, d = 3, then the 4th term is 11." : "T",
    "A geometric progression can have negative terms." : "T",
    "The common ratio in G.P. is always a positive number." : "F",
}

ch6 = {
    "The slope of a vertical line is zero." : "F",
    "The slope of a horizontal line is zero." : "T",
    "The equation of x-axis is y = 0." : "T" ,
    "The point (3, –2) lies in the fourth quadrant." : "T",
    "Two lines with slopes m₁ and m₂ are perpendicular if m₁·m₂ = –1." : "T",
}

ch7 = {
    "limₓ→0 (sin x)/x = 1." : "T",
    "The derivative of x² is 2x." : "T",
    "The limit of a constant is the constant itself." : "T",
    "The derivative of a constant is zero." : "T"
}

ch8 = {
    "The probability of an impossible event is 1." : "F",
    "The probability of a sure event is 1." : "T",
    "The sum of probabilities of all outcomes in a sample space is 1." : "T"
}

while True:
    chapters = int(input("Enter the number of chapters in numbers (99 to quit) : "))
    if chapters == 99 :
        quit()
        break
    elif chapters > 8 or chapters < 0:
        print("Only 8 chapters are avalable.")
    else:
        try:
            cha = [ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8]
            chwant = []
            for i in range(0,chapters):
                chwant.append(cha[i])
                for chap in chwant :
                    for qa in chap :
                        q_a[qa] = chap[qa]

            score = 0 
            wrong = {}

            questions = list(q_a.keys())
            random.shuffle(questions)
            for question in questions :
                print(question)
                while True:
                    try :
                        ans = input("ANS : ").upper()
                        if ans == "T" or ans == "F":
                            break
                        else :
                            print("Type carefully.")

                    except KeyboardInterrupt :
                        print("Type carefully.")
                if ans == q_a[question] :
                    score += 1
                else :
                    wrong[question] = q_a[question]

            print(f"You got {score} questions right in {len(questions)} question.")
            check = input("Do you want to check the wrong questions ? : ")
            if check == "yes" :
                for question in list(wrong):
                    print(f"Q - {question}\nANS - {q_a[question]}")
            elif check == "no" :
                pass
            else:
                print("YES OR NO")
        except ValueError:
            print("Please enter only number.")