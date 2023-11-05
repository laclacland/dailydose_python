import datetime


def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def calculate_age_in_days(birthdate):
    today = datetime.date.today()
    age_in_days = (today - birthdate).days
    return age_in_days


def create_personalized_message(age, age_in_days):
    message = (
        f"\033[1;34m ˚✧₊⁎ Happy {age}th Birthday! ⁎⁺˳✧༚ \033[0m\n"
        f"\033[1;35m      You were born {age_in_days} days ago! \033[0m"
    )
    return message


while True:
    try:
        birthdate = input("Enter your birthday (YYYY-MM-DD): ")
        year, month, day = map(int, birthdate.split('-'))
        user_birthday = datetime.date(year, month, day)
        break
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")


personalized_message = create_personalized_message(
    calculate_age(user_birthday),
    calculate_age_in_days(user_birthday))
print(personalized_message)
