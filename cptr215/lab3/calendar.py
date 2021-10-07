def day_of_week_num(user_year2, user_month2):
    if user_month2 == 1:
        user_month2 = 13
        user_year2 -= 1

    if user_month2 == 2:
        user_month2 = 14
        user_year2 -= 1

    q = 1  # day
    m = user_month2
    k = user_year2 % 100
    j = user_year2 // 100
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    result = (h % 7)
    return result


def leap_year_check(year):
    is_leap_year = False

    input_year = year

    input_yr_result = input_year % 4  # is the year a leap year
    input_century_q = input_year // 100  # is the input a century year?

    if input_yr_result == 0:
        if (input_century_q % 4) == 0:
            # print(str(input_year) + " - leap year")
            return True
        else:
            # print(str(input_year) + " - not a leap year")
            return False
    else:
        # print(str(input_year) + " - not a leap year")
        return False


user_input = input().split()  # bring in month and year
user_month = int(user_input[0])  # user inputted month
user_year = int(user_input[1])  # user inputted year


start_day_num = (day_of_week_num(user_year, user_month)) - 1

num_days_in_month = 0
num_days_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31,
        12: 30
    }

if leap_year_check(user_year) and user_month == 2:  # finds how many days in month if leap year
    num_days_in_month = 29
else:
    num_days_in_month = num_days_dict[user_month]


month_name_list = (
    "", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")

# the generic header text for the calendar
month_name_out = month_name_list[user_month]
header = (month_name_out + " " + str(user_year))
if user_month == 1:
    print("   ", header)
else:
    print("  ", header)
# gets the month name
# print(str(header).center(20))  # centers the month name

print("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")  # prints the day names

rand_counter = 0
# the loop to print the calendar days
if start_day_num < 0:
    start_day_num = 6
    rand_counter = 1
count = 7 - start_day_num
space_count = 0
print(" ", end='')

for day in range(1, num_days_in_month+1):
    if count == 0:
        print()
        count = 7
        space_count = 1
    count -= 1
    if day == 1:
        spaces = " " * (start_day_num*3)
        print(spaces, end='')
    if day > 9:
        if day == num_days_in_month:
            print(day, end="")
        else:
            if count == 0:
                print(day, end='')
            else:
                print(day, "", end='')
    elif day == 9:
        if count == 0:
            print(day, end='')
        else:
            print("", day, "", end='')
    elif day < 10 and space_count == 1:
        if count == 0:
            print(day, end='')
        else:
            print("", day, "", end='')
    else:
        if count == 0:
            print(day, end='')
        else:
            if day == num_days_in_month:
                print(day, end="")
            else:
                print(day, ' ', end='')

if rand_counter == 1:
    count += 1
else:
    print()
    print()

# 3. write tests
