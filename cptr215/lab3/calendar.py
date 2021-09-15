def day_of_week_num(year, month, day):
    if month == 1:
        month = 13
        year -= 1

    if month == 2:
        month = 14
        year -= 1

    q = day
    m = month
    k = year % 100
    j = year // 100
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


#def starting_day()


user_input = input("Input the month and year: ").split()
user_month = int(user_input[0])
user_year = int(user_input[1])

month_name_list = ("", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print("      ", month_name_list[user_month])
print("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")