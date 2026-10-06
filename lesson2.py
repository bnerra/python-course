#-- FUNCTIONS AND LOOPS --#

# Part A: Functions #

def greet(name):
    return f"Hello, {name}!"

message = greet("Nick")
print(message)


#-Default Parameter Values-#
def greetings(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greetings("Nick"))
print(greetings("Nick", "Hey"))

# Part B: for loops #

temps = [72, 90, 45]
for t in temps:
    print(t)

# To loop a set number of times, use range() #

for i in range(5):
    print(i)

# Part C: while loops (quick) #

count = 3
while count > 0:
    print(count)
    count -= 1

# EXERCISE #
# 1. Turn your weather logic into a function called describe_weather that takes a temperature and returns the message ("Hot one today." etc.). Don't print inside the function.
# 2. Make a list of temperatures: [90, 85, 84.5, 72, 60, 59.9, 40].
# 3. Loop over the list and, for each one, print a line like:
#    90 degrees: Hot one today.

NICE = 'Nice weather.'

def describe_weather(temperature):
    if temperature >= 85:
        return "Hot one today."
    elif temperature >= 60:
        return NICE
    else:
        return "Grab a jacket."

temperatures = [90, 85, 84.5, 72, 60, 59.9, 40]

counter = 0

for t in temperatures:
    message = describe_weather(t)
    print(f"{t} degrees: {message}")
    if message == NICE:
        counter += 1

print(f"Count: {counter}")