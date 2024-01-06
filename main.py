'''Python module for working with dates and times.'''
from datetime import date, datetime


def get_birthdays_per_week(users: dict) -> dict:
    '''
    Function to display a list of colleagues who need 
    to be congratulated on their birthday for the week.
    '''
    today = date.today()

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    for user in users:

        name = user['name']

        birthday_this_year = user['birthday'].replace(year=today.year)
        birthday_next_year = user['birthday'].replace(year=today.year + 1)

        delta_days_this_year = (birthday_this_year - today).days
        delta_days_next_year = (birthday_next_year - today).days

        day_of_week = None

        if 0 <= delta_days_this_year <= 7:
            day_of_week = birthday_this_year.strftime('%A')
        if 0 <= delta_days_next_year <= 7:
            day_of_week = birthday_next_year.strftime('%A')

        if day_of_week is not None :
            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                day_of_week = 'Monday'
            birthdays_per_week[day_of_week].append(name)

    # regenerate dict without empty days
    birthdays_per_week = {day: names for day, names in birthdays_per_week.items() if names}

    return birthdays_per_week


if __name__ == "__main__":
    employees = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(employees)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
