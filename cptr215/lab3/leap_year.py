is_leap_year = False

input_year = int(input())

input_yr_result = input_year % 4  # is the year a leap year
input_century_q = input_year // 100  # is the input a century year?

if input_yr_result == 0:
    if (input_century_q % 4) == 0:
        print(str(input_year) + " - leap year")
    else:
        print(str(input_year) + " - not a leap year")
else:
    print(str(input_year) + " - not a leap year")
