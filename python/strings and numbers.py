# print (9)
print("20 days are " + " " + str(20 * 24 * 60) + " " + "minutes")

# or

print(f"20 days are {20 * 24 * 60} minutes")

# variables are containers for storing values
# python is dynamically typed

calculation_to_seconds = 24 * 60 * 60

print(f"20 days are {20 * calculation_to_seconds} seconds")


# instead of repeating same logic we can use functions

def days_to_units():
    print(f"20 days are {20 * calculation_to_seconds} seconds")
    print("function now executed correctly")


days_to_units()


#pass variables or arguments into functions

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {20 * calculation_to_seconds} seconds")
    print("function now executed correctly with arguments")


days_to_units(90)