import json
from datetime import datetime

with open('sample-sets.json') as file:
    data = json.load(file)

# global variables
lc_travel = 45
hc_travel = 55
lc_full = 75
hc_full = 85

def calc(ex_set): # ex_set is list of dicts
    total = 0

    for proj in ex_set: # each project is a dict

        cc = proj["city_cost"]
        sd = proj["start_date"]
        ed = proj["end_date"]
        sday = sd.day
        eday = ed.day

        if cc == "low": # low cost city
            if sd == ed: # one day project
                total += lc_travel
            else:
                between = eday - sday - 1
                total += (2 * lc_travel)
                total += (between * lc_full)
        else: # high cost city
            if sd == ed: # one day project
                total += hc_travel
            else:
                between = eday - sday - 1
                total += (2 * hc_travel)
                total += (between * hc_full)

    return str(total)


for set in data:

    for project in data[set]:

        # change start date string to datetime object
        start_val = [value for value in project.values()][2]
        dt_start = datetime.strptime(start_val, '%m/%d/%y')
        project["start_date"] = dt_start

        # change end date string to datetime object
        end_val = [value for value in project.values()][3]
        dt_end = datetime.strptime(end_val, '%m/%d/%y')
        project["end_date"] = dt_end

    # sort projects in order of increasing start date
    sorted_set = sorted(data[set], key=lambda d: d['start_date']) 

    # after projects in set are sorted, run reimbursement calculation on set
    ret_str = "The reimbursement amount for " + set + " is $" + calc(data[set])
    print(ret_str)
