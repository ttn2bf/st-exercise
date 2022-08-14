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
    prev_cc = "string"
    prev_sd = "string"
    prev_ed = "string"
    prev_full = False

    for proj in ex_set: # each project is a dict

        pn = proj["proj_num"]
        cc = proj["city_cost"]
        sd = proj["start_date"]
        ed = proj["end_date"]
        sday = sd.day
        eday = ed.day
        delta = ed - sd

        if pn == "Project 1": # for the first project in the set
            between = delta.days - 1
            if cc == "low": # low cost city
                if sd == ed: # one day project
                    total += lc_travel
                else:
                    total += (2 * lc_travel)
                    total += (between * lc_full)
            else: # high cost city
                if sd == ed: # one day project
                    total += hc_travel
                else:
                    total += (2 * hc_travel)
                    total += (between * hc_full)
                    
        else: # for sequential projects, need previous project info
            between = delta.days - 1
            gap = (sd - prev_ed).days - 1
            leftover = delta.days - (abs(gap)) + 1
            if cc == "low": # low cost city
                if sd == ed: # one day project
                    if gap == 0: # next to another project
                        if prev_cc == "low": # previous low cost city
                            if prev_full == True:
                                total += lc_full
                            else: 
                                total -= lc_travel
                                total += (2 * lc_full)
                        else: # previous high cost city
                            if prev_full == True:
                                total += lc_full
                            else:
                                total -= hc_travel
                                total += (hc_full + lc_full)
                        prev_full = True
                    elif gap < 0: # overlap
                        if prev_cc == "low":
                            if prev_full == False:
                                total -= lc_travel
                                total += lc_full
                        else:
                            if prev_full == False:
                                total -= hc_travel
                                total += hc_full
                        prev_full = True
                    else:
                        total += lc_travel
                        prev_full = False
                else: # multiple days
                    if gap == 0: # next to another project
                        if prev_cc == "low": # previous low cost city
                            if prev_full == True:
                                total += lc_travel
                                total += (delta.days * lc_full)
                            else:
                                total += ((delta.days + 1) * lc_full)
                        else: # previous high cost city
                            if prev_full == True:
                                total -= hc_travel
                                total += lc_travel
                                total += (delta.days * lc_full)
                            else:
                                total -= hc_travel
                                total += (hc_full + lc_travel)
                                total += (delta.days * lc_full)
                        prev_full = False
                    elif gap < 0: # overlap
                        if prev_cc == "low":
                            if leftover >= 1:
                                if prev_full == True:
                                    total += ((leftover - 1) * lc_full)
                                    total += lc_travel
                                else:
                                    total += lc_full
                                    total += ((leftover - 1) * lc_full)
                            elif leftover == 0:
                                if prev_full == False:
                                    total -= lc_travel
                                    total += lc_full
                                prev_full = True
                        else:
                            if leftover >=1:
                                if prev_full == True:
                                    total += ((leftover - 1) * lc_full)
                                    total += lc_travel
                                else:
                                    total -= hc_travel
                                    total += hc_full
                                    total += ((leftover - 1) * lc_full)
                                    total += lc_travel
                            elif leftover == 0:
                                if prev_full == False:
                                    total -= hc_travel
                                    total += hc_full
                                prev_full = True
                    else:
                        total += (2 * lc_travel)
                        total += (between * lc_full)
                        prev_full = False

            else: # high cost city
                if sd == ed: # one day project
                    if gap == 0: # next to another project
                        if prev_cc == "low": # previous low cost city
                            if prev_full == True:
                                total += hc_full
                            else:
                                total -= lc_travel
                                total += (lc_full + hc_full)
                        else: # previous high cost city
                            if prev_full == True:
                                total += hc_full
                            else:
                                total -= hc_travel
                                total += (2 * hc_full)
                        prev_full = True
                    elif gap < 0: # overlap
                        if prev_full == False:
                            total -= hc_travel
                            total += hc_full
                        prev_full = True
                    else:
                        total += lc_travel
                        prev_full = False
                else: # multiple days
                    if gap == 0: # next to another project
                        if prev_cc == "low": # previous low cost city
                            if prev_full == True:
                                total += hc_travel
                                total += (delta.days * hc_full)
                            else:
                                total -= lc_travel
                                total += (lc_full + hc_travel)
                                total += (delta.days * hc_full)
                        else: # previous high cost city
                            if prev_full == True:
                                total += hc_travel
                                total += (delta.days * hc_full)
                            else:
                                total += ((delta.days + 1) * hc_full)
                        prev_full = False
                    elif gap < 0: # overlap
                        if prev_cc == "low":
                            if leftover >= 1:
                                if prev_full == True:
                                    total -= (abs(gap) * lc_full)
                                    total += (abs(gap) * hc_full)
                                    total += ((leftover - 1) * hc_full)
                                    total += hc_travel
                                else:
                                    total -= lc_travel
                                    total -= ((abs(gap) - 1) * lc_full)
                                    total += (abs(gap) * hc_full)
                                    total += ((leftover - 1) * hc_full)
                                    total += hc_travel
                            elif leftover == 0:
                                if prev_full == True:
                                    total -= (abs(gap) * lc_full)
                                    total += (abs(gap) * hc_full)
                                    total += ((leftover - 1) * hc_full)
                                    total += hc_travel
                                else:
                                    total -= lc_travel
                                    total -= ((abs(gap) - 1) * lc_full)
                                    total += (abs(gap) * hc_full)
                                    total += ((leftover - 1) * hc_full)
                                    total += hc_full
                                prev_full = True
                        else:
                            if leftover >= 1:
                                if prev_full == True:
                                    total += ((leftover - 1) * hc_full)
                                    total += hc_travel
                                else:
                                    total += hc_full
                                    total += ((leftover - 1) * hc_full)
                            elif leftover == 0:
                                if prev_full == False:
                                    total -= hc_travel
                                    total += hc_full
                    else: 
                        total += (2 * hc_travel)
                        total += (between * hc_full)
                        prev_full = False
        
        # set current project info as previous project info before moving onto next project
        prev_cc = cc
        prev_sd = sd
        prev_ed = ed

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
