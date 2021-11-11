total_money = 0

first_job_time = int(input("how much do you work at you first job? "))
first_job_pay = float(input("how much do you make? "))
total_money += first_job_pay * first_job_time

second_job_time = int(input("how much do you work at your second job? "))
second_job_pay = float(input("how much do you get payed? "))
total_money += second_job_pay * second_job_time

total_money *= 15

print(f"You currently make ${total_money} per semester.")

weekly_income = total_money / 15
ten = weekly_income / 10
twelve = weekly_income / 12
thirteen = weekly_income / 13
fifteen = weekly_income / 15

print(f"You would need to work {ten} hours per week to get the same amount working $10/hr")
print(f"You would need to work {twelve} hours per week to get the same amount working $12/hr")
print(f"You would need to work {thirteen} hours per week to get the same amount working $13/hr")
print(f"You would need to work {fifteen} hours per week to get the same amount working $15/hr")
