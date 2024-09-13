temperatures = []

print(type(temperatures))

temperatures = [23.4, 34.5, 45.6, 56.7, 67.8]

print(temperatures)

employee_information = [
    "A123",
    23456.34,
    123,
    False
]

# Java
# float[] temperatures;

print(employee_information)

employee_data = [
    ["B234", 23406.34, 5849, True],
    employee_information
]

print(employee_data)

print(employee_information[1])
print(type(employee_information[1]))

print(employee_data[1][1])
print(type(employee_data[1][1]))

employee_information[1] = 99999.99

print(employee_information)

# List Functions
number_of_elements = len(temperatures)

print(len("Damien"))

temperatures.append(24.5)
temperatures.insert(3, 14.6)
temperatures.remove(24.5)
last_temperature = temperatures.pop()
index = temperatures.index(14.6)
temperatures.sort()
temperatures.reverse()
