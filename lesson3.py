# LISTS AND DICTIONARIES #
# Part A: Lists #

temps = [72, 90, 45]

print(temps[0])     # 72 -- first item
print(len(temps))   # 3
temps.append(60)    # like push() in JS

print(temps[-1])    # 45 -- last item
print(temps[-2])    # 90 -- second to last item

nums = [10, 20, 30, 40, 50]

print(nums[1:3])    # [20, 30]
print(nums[:2])     # [10, 20] -- from the start
print(nums[2:])     # [30, 40, 50] -- to the end

# 'in' is like .includes() in JS #
if 90 in temps:
    print("Found it")

# Part B: Dictionaries #

city = {"name": "St. Louis", "temp": 72}

print(city["name"])     # St. Louis
city["temp"] = 75       # update a value
city["state"] = "MO"    # add a new key

# note: keys need quotes, and you can't use dot notation --> city["name"] #
# note: missing keys are an error, not undefined. e.g., city["zip"] crashes with a KeyError. Use .get() #

print(city.get("zip"))            # None — no crash
print(city.get("zip", "unknown")) # "unknown" — your fallback

# .items() gives you each key and value as a pair #
for key, value in city.items():
    print(f"{key}: {value}")

# Part C: List comprehensions #
long_hot = []
for t in temps:
    if t >= 85:
        long_hot.append(t)

hot = [t for t in temps if t >= 85]

doubled = [t * 2 for t in temps]


# EXERCISE #

# 1. Create a list of dictionaries, where each dict is a city with a "name" and "temp". Use at least 4 cities with a mix of temperatures, for example {"name": "St. Louis", "temp": 72}.
# 2. Loop over the list and print each city's report:
#    St. Louis: 72 degrees. Nice weather.
# 3. Use a list comprehension to build a list of just the names of cities that are 85 or hotter, then print it.
# 4. Print the last city in the list using negative indexing.

# Bonus: add one city that's missing its "temp" key entirely. Make your loop handle it without crashing, printing something like Chicago: no temperature data. instead. (Hint: .get().)

def describe_weather(temperature):
    if temperature >= 85:
        return "Hot one today."
    elif temperature >= 60:
        return "Nice weather."
    else:
        return "Grab a jacket."

cities = [{"name": "Phoenix", "temp": 92}, {"name": "St. Louis", "temp": 71}, {"name": "Chicago", "temp": 67}, {"name": "Miami", "temp": 90}, {"name": "San Francisco"}]


for c in cities:
    temperature = c.get("temp")
    if temperature is None:
        print(f"{c['name']}: no temperature data.")
    else:
        message = describe_weather(temperature )
        print(f"{c['name']}: {temperature} degrees. {message}")

hot_cities = [c["name"] for c in cities if c.get("temp") is not None and c.get("temp") >= 85]

print(hot_cities)
print(cities[-1]["name"])



