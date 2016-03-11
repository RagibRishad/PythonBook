
# Calculating average of 3 exams scores

def exam_score():
    score1 = eval(input("First exam score: "))
    score2 = eval(input("Seconed exam score "))
    score3 = eval(input(("Third exam score: ")))

    average = (score1+score2+score3) / 3

    print("The average score is:",average)

if __name__ == '__main__':
    exam_score()