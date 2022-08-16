calculation_to_hours = 24
num_of_unit = "hours"


# pass variables or arguments into functions

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {num_of_unit}"
    return "function now executed correctly"


user_input = input("Hey there ! please enter number of days to know in hours \n")
user_input_number=int(user_input)  #changing one data typr to another is called type casting
print(user_input_number)
calculated_value = days_to_units(user_input_number)

print(calculated_value)

#ifelse statements in funcitons if the user gives nonsense values

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {num_of_unit}"
        return "function now executed correctly"
    else:
        return "you entered a wrong value please try again giving positive values"


user_input = input("Hey there ! please enter number of days to know in hours \n")
user_input_number=int(user_input)  #changing one data typr to another is called type casting
print(user_input_number)
calculated_value = days_to_units(user_input_number)

print(calculated_value)