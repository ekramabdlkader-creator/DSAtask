def is_leap(year: int) -> bool:
    """Return True if `year` is a leap year using Gregorian rules.

    A year is a leap year if it is divisible by 4, except years divisible by 100
    are not leap years unless they are also divisible by 400.

    Raises:
        TypeError: if `year` is not an int.
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    # Simple demonstration / smoke tests
    test_years = [2000, 1900, 2100, 2020]
    for y in test_years:
        print(f"is {y} a leap year? {is_leap(y)}")
