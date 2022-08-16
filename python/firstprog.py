calculation_to_hours = 24
num_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {num_of_unit}"
        return "function now executed correctly"
    elif num_of_days == 0:
        return "you entered zero value please give other than Zero"
    else:
        return "you entered Negative value please try again giving positive values"


user_input = input("Hey there ! please enter number of days to know in hours \n")
user_input_number = int(user_input)  # changing one data type to another is called type casting
print(user_input_number)
calculated_value = days_to_units(user_input_number)
print(calculated_value)
