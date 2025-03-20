#to find the CGPA 
print('\n\tFIND TOTAL CGPA AND PERCENTAGE OF YOUR DEGREE\n\n')

years = int(input('How many years your degree? '))
print('\n\n')
semister = int(input('Each year how many semisters are conducted(like 1,2 or 3): '))
print('\n\n')
year = 1
value = True
semister_score_list = []
credit_score_list = []
while value:
    sem_count = semister
    sem = 1 
    semister_score = 0
    while sem_count > 0:
        print(f'\n\tEnter Year {year} deatils\n')
        subjects = int(input(f'How many subjects do you have in  sem-{sem} : '))
        print('\n')
        subject = 1
        total = 0
        credit_score = 0
        while subjects > 0:
            print(f"please enter subject {subject} details \n")
            gradepoints = float(input(f'Enter subject {subject} grade(out of 10) : '))
            credits = float(input(f'Enter subject {subject} credits : '))
            value = (gradepoints * credits)
            total += value
            credit_score += credits
            subject += 1
            subjects = subjects - 1
        semister_score = total/credit_score
        print(f'SCGPA of sem - {sem} is {semister_score}')
        semister_score_list.append(semister_score)
        credit_score_list.append(credit_score)
        sem += 1
        sem_count = sem_count - 1
    years = years - 1
    year += 1
    if years > 0:
        value = True
    else:
        value = False
print(semister_score_list)
print(credit_score_list)
total_q_score = 0
for i in range(len(semister_score_list)):
    q_score = semister_score_list[i]*credit_score_list[i]
    total_q_score += q_score
total_d_score = 0
for j in range(len(credit_score_list)):
    d_score = credit_score_list[i]
    total_d_score += d_score

cummulative_score = total_q_score/total_d_score

print(f'The CGPA is {cummulative_score}')


        


