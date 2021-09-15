def day_of_week_num(user_year, user_month):
    if user_month == 1:
        user_month = 13
        user_year -= 1

    if user_month == 2:
        user_month = 14
        user_year -= 1

    q = 1 # day
    m = user_month
    k = user_year % 100
    j = user_year // 100
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    result = (h % 7)
    return result


def day_of_week_word(day_num):
    day_name_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    day_of_week = day_name_dict[day_num]
    return day_of_week


def leap_year(year):
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


def num_days():
    # some code here to determine the number of day in a month



user_input = input("Input the month and year: ").split()
user_month = int(user_input[0])
user_year = int(user_input[1])

start_day_num = day_of_week_num(user_year, user_month)
month_start_day = day_of_week_word(start_day_num)

month_name_list = ("", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print("      ", month_name_list[user_month])
print("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")
for day in range(user_month):
    print(day, '')



# objective
# 1. find number of days in a month
#         - is leap year?
#         - is feb?
# 2. print the first of the month under the correct day with spaces as a string which then mulipies by the amount of days before the start day.