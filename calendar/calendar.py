import datetime


def print_calendar(year):
    for month in range(1, 13):
        month_calendar = datetime.date(year, month, 1)
        print("\n" + month_calendar.strftime("%B %Y"))
        print("Mo Tu We Th Fr Sa Su")

        # Find the weekday of the first day of the month
        weekday_of_first_day = month_calendar.weekday()

        # Print leading spaces for the first week
        print("   " * weekday_of_first_day, end="")

        # Print the days of the month
        while month_calendar.month == month:
            print(f"{month_calendar.day:2d} ", end="")
            if month_calendar.weekday() == 6:  # Sunday, start a new line
                print()
            month_calendar += datetime.timedelta(days=1)

        # Print a new line after the last week
        print()


# Get user input for the year
year = int(input("Enter year: "))

# Call the function to print the calendar
print_calendar(year)
