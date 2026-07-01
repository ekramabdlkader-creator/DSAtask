def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print("is 2000 a leap year?", is_leap(2000))  
print("is 1900 a leap year?", is_leap(1900))
print("is 2100 a leap year?", is_leap(2100))
print("is 2020 a leap year?", is_leap(2020))