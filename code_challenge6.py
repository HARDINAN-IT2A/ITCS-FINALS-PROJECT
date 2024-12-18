prelim = eval(input ("PRELIM GRADE: "))
midterm = eval (input("MIDTERM GRADE: "))
semi = eval(input("SEMI FINALS GRADE: "))
finals = eval(input("FINALS GRADE: "))
quiz = eval (input("QUIZ GRADE: "))
project = eval(input ("PROJECT GRADE: "))

total = (prelim * 0.15) + (midterm * 0.15) + (semi * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

if total >=75 and total <=100:
	print("Congratulation! You have passed the subject.")

elif total < 0 or total > 100:
	print("Sorry, you have failed the subject")