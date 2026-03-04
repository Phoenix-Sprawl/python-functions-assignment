#Task 1 - Process the scores
students = {
    "Sara": [96,98,93],
    "Ajay": [84,72,86],
    "Bala": [35,38,59],
    "Tony": [85,91,77]
}

def process_scores(students):
  averages = {}
  for name, scores in students.items():
    average_score = round((sum(scores)/len(scores)),2)
    averages[name]=average_score
  return(averages)

#Task 2 - Classify the Grades
def classify_grades(averages):
  classified={}
  A_MIN = 90
  B_MIN = 75
  C_MIN = 60

  for name, average in averages.items():
    if average >= A_MIN:
      grade = 'A'
    elif average >= B_MIN:
      grade = 'B'
    elif average >= C_MIN:
      grade = 'C'
    else:
      grade = 'F'

    classified[name] = [average,grade]
  return(classified)


#Task 3 - Generate the Report
def generate_report(classified, passing_avg=70):
  total_students = 0
  pass_count = 0
  fail_count = 0

  print(f"===== Student Grade Report =====")
  for name, (average,grade) in classified.items():
    total_students += 1
    if average >= passing_avg:
      status = 'PASS'
      pass_count += 1
    else:
      status = 'FAIL'
      fail_count += 1
    print(f"{name}  | Avg: {average} | Grade: {grade} | Status: {status}")
    
  print("================================") 
  
  print(f"""
  Total Students: {total_students}
  Passed        : {pass_count}
  Failed        : {fail_count}
  """)
  return pass_count


#main block
def main():
  averages = process_scores(students)
  classified = classify_grades(averages)
  generate_report(classified)

grade_analyzer = main()