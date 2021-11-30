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
    input_year = year

    input_yr_result = input_year % 4  # is the year a leap year
    input_century_q = input_year // 100  # is the input a century year?

    if input_yr_result == 0:
        if (input_century_q % 4) == 0:
            return True
        else:
            return False
    else:
        return False


num_days_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def calendar(month, year):
    start_day_num = (day_of_week_num(year, month)) - 1

    if leap_year_check(year) and month == 2:  # finds how many days in month if leap year
        num_days_in_month = 29
    else:
        num_days_in_month = num_days_dict[month]

    month_name_list = (
        "", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November",
        "December")

    # the generic header text for the calendar
    month_name_out = month_name_list[month]
    header = (month_name_out + " " + str(year))

    # gets the month name and centers it
    str(header).center(20)
    k = 0
    my_string = str(header).center(20)
    left_filler = ""
    for i in my_string:
        k += 1
        if i != " ":
            left_filler = (k - 2) * " "
            break

    print(left_filler, str(header))
    print("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")  # prints the day names

    rand_counter = 0
    # the loop to print the calendar days
    if start_day_num < 0:
        start_day_num = 6
        rand_counter = 1
    count = 7 - start_day_num
    space_count = 0
    print(" ", end='')

    for day in range(1, num_days_in_month + 1):
        if count == 0:
            print()
            count = 7
            space_count = 1
        count -= 1
        if day == 1:
            spaces = " " * (start_day_num * 3)
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
                print("", day, end='')
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
        print()
    else:
        print("")
        print("")


def daysInMonth(month, year):
    if leap_year_check(year) and month == 2:  # finds how many days in month if leap year
        num_days_in_month = 29
    else:
        num_days_in_month = num_days_dict[month]
    return num_days_in_month


def startingDayOfWeek(month, year):
    start_day_num = (day_of_week_num(year, month))
    if start_day_num == 0:
        start_day_num = 7
    return start_day_num


def monthCalendarFor(month, year):
    result = ""
    start_day_num = (day_of_week_num(year, month)) - 1

    if leap_year_check(year) and month == 2:  # finds how many days in month if leap year
        num_days_in_month = 29
    else:
        num_days_in_month = num_days_dict[month]

    month_name_list = (
        "", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November",
        "December")

    # the generic header text for the calendar
    month_name_out = month_name_list[month]
    header = (month_name_out + " " + str(year))

    # gets the month name and centers it
    str(header).center(20)
    k = 0
    my_string = str(header).center(20)
    left_filler = ""
    for i in my_string:
        k += 1
        if i != " ":
            left_filler = (k - 2) * " "
            break

    result += (left_filler + " ")
    result += f"{str(header)}\n"
    result += f"Su Mo Tu We Th Fr Sa\n"

    rand_counter = 0
    # the loop to print the calendar days
    if start_day_num < 0:
        start_day_num = 6
        rand_counter = 1
    if start_day_num == 0:
        start_day_num = 0
        rand_counter = 3

    count = 7 - start_day_num
    space_count = 0
    result += " "

    for day in range(1, num_days_in_month + 1):
        if count == 0:
            result += f"\n"
            count = 7
            space_count = 1
        count -= 1
        if day == 1:
            spaces = " " * (start_day_num * 3)
            result += str(spaces)
        if day > 9:
            if day == num_days_in_month:
                result += str(day)
            else:
                if count == 0:
                    result += str(day)
                else:
                    result += (str(day) + " ")
        elif day == 9:
            if count == 0:
                result += str(day)
            else:
                result += (" " + str(day) + " ")
        elif day < 10 and space_count == 1:
            if count == 0:
                result += (" " + str(day))
            else:
                result += (" " + str(day) + " ")
        else:
            if count == 0:
                result += str(day)
            else:
                if day == num_days_in_month:
                    result += str(day)
                else:
                    result += (str(day) + "  ")

    if rand_counter == 1:
        result += "\n"
    elif rand_counter == 3:
        result += "\n"
        result += "\n"
        result += "\n"
    else:
        result += "\n"
        result += "\n"

    return result

# TESTS:
# print(calendar(5, 2002))
# print(startDayNum(5, 2002))
# print(monthCalendarFor(1, 2000))
# print(startingDayOfWeek(1, 2000))
# print(monthCalendarFor(2, 1981))
# for x in range(1, 7):
#     print(startingDayOfWeek(x, 2000))
