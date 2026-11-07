#list and tuples created to hold student score and grades for the scores
quiz_score = []
grades = ('A', 'B', 'C', 'D', 'F')

#input statement to collect user anme and quiz score information
student_name = input("Good day, Pleae enter you name.\n")
for value in range(5):
    quiz_score_input = int(input("Please enter your grade score ranging from 0 to 100\n"))
    quiz_score.append(quiz_score_input)

#calculation to find the avergae of scores using len and sum of quiz scores
number_of_subjects = len(quiz_score)
total_score = sum(quiz_score)
average = total_score / int(number_of_subjects) 

#messages that will be displayed at the end of the report card output
message1 = f"Excelent {student_name}, you have a bright futer ahead."
message2 = f"Great job {student_name}, keep up the good work."
message3 = f"Good Effort {student_name}, but i believe you can achieve greater."
message4 = f"Hm, {student_name} I know you can do better."
message5 = f"GG Fam, it's time to pack it up {student_name}"

#conditional statements used to compare average with grade requirments
if average >= 90 or average >= 100:
    print(f"==== Grade Report ==== \nStudent: {student_name} \nScores: {quiz_score} \nAverage: {average} \nGrade: {grades[0]} \n{message1} \n======================")
elif average >= 80 or average >= 89:
    print(f"==== Grade Report ==== \nStudent: {student_name} \nScores: {quiz_score} \nAverage: {average} \nGrade: {grades[1]} \n{message2} \n======================")
elif average >= 70 or average >= 79:
    print(f"==== Grade Report ==== \nStudent: {student_name} \nScores: {quiz_score} \nAverage: {average} \nGrade: {grades[2]} \n{message3} \n======================")
elif average >= 60 or average >= 69:
    print(f"==== Grade Report ==== \nStudent: {student_name} \nScores: {quiz_score} \nAverage: {average} \nGrade: {grades[3]} \n{message4} \n======================")
elif average <60 or average > 0:
    print(f"==== Grade Report ==== \nStudent: {student_name} \nScores: {quiz_score} \nAverage: {average} \nGrade: {grades[4]} \n{message5} \n======================")
else:
    print(" you have typed an invlid score")
