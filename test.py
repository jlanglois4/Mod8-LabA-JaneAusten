ages = [{'Matt': 30, 'Katie': 29}, {'Nik': 31, 'Jack': 43,}, {'Alison': 32, 'Kevin': 38}]

max_age = int()

for dict in ages:
    if max(dict.values()) > max_age:
        max_age = max(dict.values())

print(max_age)