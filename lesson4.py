# COMMON PYTHON GOTCHAS #

# Gotcha 1: Division #
print(7 / 2)        # 3.5
print(7 // 2)       # 3
print(-7 // 2)      # -4

# / always gives a float, even 4 / 2 is 2.0
# // is floor division, which rounds down, not toward zero. So -7 // 2 is -4, not -3
# % (remainder) follows the same rule: -7 % 2 is 1 in Python, but -1 in JS


# Gotcha 2: Copying a list (aliasing) #
original = [1, 2, 3]
copy = original
copy.append(4)
print(original)     # [1, 2, 3, 4]

# copy = original doesn't copy anything. Both names point to the same list, so changing one changes "both".
# This works the same way in JS with arrays and objects.

# To actually copy:
copy = original.copy()      # or original[:]


# Gotcha 3: Mutable default arguments #
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))    # ['a']
print(add_item("b"))    # ['a', 'b']


# The standard fix:
def adding_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# Rule: never use a list, dict, or other mutable value as a default. Use None and create it inside.

# Gotcha 4: Changeing a list while looping over it #
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)                 # [1, 2, 3]

# One 2 survives. When you remove an item, everything shifts left, and the loop skips over the next item.
# The fix is to build a new list instead, which is a perfect job for a comprehension:
numbers = [n for n in nums if n != 2]

print(numbers)      # [1, 3]

# Gotcha 5: is vs == #
# == asks: do these have the same value?
# is asks: are these the exact same object in memory?
a = [1, 2]
b = [1, 2]
print(a == b)       # True -- same contents
print(a is b)       # False -- two separate lists

# Use is only for None (and True/False). For everything else, use ==.


# Gotcha 6: Truthiness (recap) #
# None, 0, 0.0, "", [], and {} are all falsy.
# if value: and if value is not None: are not the same check.


# EXERCISE #

# The prompt given to the AI:
#   Write a function average_scores(students) that takes a list of dicts, each with a "name" and an optional "scores" list.
#   Return a dict mapping each student's name to their average score.
#   Students with no scores, or an empty scores list, should map to None.

# The AI's response:
def average_scores(students, results={}):
    for s in students:
        scores = s["scores"]
        if scores:
            results[s["name"]] = sum(scores) // len(scores)
        else:
            results[s["name"]] = 0
    return results

# 1. Find every bug you can. There are four (one is a crash, the others are wrong results).
# 2. For each one, write a sentence or two: what's wrong, an input that exposes it, and what should happen instead.
#    Be specific, as covered earlier: name the line, show the failing input.
# 3. Then write your corrected version of the function.
# 4. After you've written your review, run both versions with some test data to confirm your findings.

# On line1 there is a bug where the parameter results is declared as an empty dict. A bug will occur on any subsequent call of average_scores which will recall the stored results dict and any changes will mutate the values. Instead, results should be defaulted to None and created new inside each time.

# On line3 there is a potential crash in the case a dict inside students is missing the "scores" key, such as students = [{"name": "John"}] and will throw KeyError. Instead, line3 should use get() with a default value of None.

# On line5 there is a potential mathematical bug calculating the average of scores. Using // is floor division which will give a rounded down value in the case the average is not a whole number, such as in the case of [90, 85]. Instead use / which will yield a float and more accurate value for average. 

# On line7 there is a bug in the else case that sets the average to 0 and should be set to None as specified in the instructions.

def average_scores(students):
    results = {}
    for s in students:
        scores = s.get("scores", None)
        if scores:
            results[s["name"]] = sum(scores) / len(scores)
        else:
            results[s["name"]] = None
    return results
