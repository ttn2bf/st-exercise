import json
from datetime import datetime

with open('sample-sets.json') as file:
    data = json.load(file)

def calc(sample_set):
    total = 0
    return str(total)


for set in data:

    for project in data[set]:

        # change start date string to datetime object
        start_val = [value for value in project.values()][2]
        dt_start = datetime.strptime(start_val, '%d/%m/%y')
        project["start_date"] = dt_start

        # change end date string to datetime object
        end_val = [value for value in project.values()][3]
        dt_end = datetime.strptime(end_val, '%d/%m/%y')
        project["end_date"] = dt_end

    # sort projects in order of increasing start date
    sorted_set = sorted(data[set], key=lambda d: d['start_date']) 

    # after projects in set are sorted, run reimbursement calculation on set
    ret_str = "The reimbursement amount for " + set + " is $" + calc(data[set])
    print(ret_str)
