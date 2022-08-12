import json
with open('sample-sets.json') as file:
    data = json.load(file)
print(data)

def calc(sample_set):
    total = 0
    return total

for set in data:
    #print(set, ": ", data[set])
    print(calc(data[set]))
