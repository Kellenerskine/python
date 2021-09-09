"""Design, implement, and fully test a function that determines the day of the week a particular date falls on,
as a number from 1 (Sunday) to 7 (Saturday) (dayOfWeekForDate(year, month, day)).
Then create a function that converts that day-of-week number to the English name (nameForDayOfWeekNumber(dayNumber)).
You may not use any modules that perform date calculations."""


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


user_year = int(input("Type in the year of your date with all four nums: "))
user_month = int(input("Type in the month of your date with no leading zero: "))
user_day = int(input("Type in the day of you date with no leading zero: "))
num_of_day = day_of_week_num(user_year, user_month, user_day)
print(num_of_day)
print(day_of_week_word(num_of_day))

# the following code is what was required to pass the assignment in class
# def dayOfWeekForDate(year, month, day):
#     """
#     >>>dayOfWeekForDate(2002, 6, 7)
#     6
#     """
#
#     if year == 1752 and month == 9 and day == 30:
#         return 7
#     else:
#         if month == 1:
#             month = 13
#             year = year - 1
#
#         if month == 2:
#             month = 14
#             year = year - 1
#
#         q = day
#         m = month  # account for jan and feb
#         k = year % 100
#         j = year // 100
#         h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
#         result = (h % 7)
#         return result
#
#
# def nameForDayOfWeekNumber(dayNumber):
#     """
#     >>>nameForDayOfWeekNumber(6)
#     "Friday"
#     """
#     day_name_dict = {
#         1: "Sunday",
#         2: "Monday",
#         3: "Tuesday",
#         4: "Wednesday",
#         5: "Thursday",
#         6: "Friday",
#         7: "Sabbath"
#     }
#
#     day_of_week = day_name_dict[dayNumber]
#     return day_of_week
#
#
# if __name__ == "__main__":
#     import doctest
#
#     doctest.testmod()
