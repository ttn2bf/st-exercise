# Simple Thread technical exercise

Given a set of projects, calculate a reimbursement amount for the set. Each project has a start date and an end date. The first day of a project and the last day of a project are always "travel" days. Days in the middle of a project are "full" days. There are also two types of cities a project can be in, high cost cities and low cost cities.

## A Few Rules
- First day and last day of a project, or sequence of projects, is a travel day.
- Any day in the middle of a project, or sequence of projects, is considered a full day.
- If there is a gap between projects, then the days on either side of that gap are travel days.
- If two projects push up against each other, or overlap, then those days are full days as well.
- Any given day is only ever counted once, even if two projects are on the same day.

## Reimbursement Rates
- A travel day is reimbursed at a rate of 45 dollars per day in a low cost city.
- A travel day is reimbursed at a rate of 55 dollars per day in a high cost city.
- A full day is reimbursed at a rate of 75 dollars per day in a low cost city.
- A full day is reimbursed at a rate of 85 dollars per day in a high cost city.

## How To Run

You can run this code on any JSON file containing data on sets of projects that fit the following criteria:

The JSON file must be in the same folder as main.py. Each set must be formatted as "Set #". Each project must have the following information:
- "proj_num" is a string formatted as "Project #"
- "city_cost" is a string containing either "low" or "high"
- "start_date" is a string containing a date formatted as "mm/dd/yy"
- "end_date" is a string containing a date formatted as "mm/dd/yy"

For example:

```
{
    "Set 1": [
        {
            "proj_num": "Project 1",
            "city_cost": "low",
            "start_date": "09/01/15",
            "end_date": "9/3/15"
        }
    ],

    "Set 2": [
        {
            "proj_num": "Project 1",
            "city_cost": "low",
            "start_date": "9/1/15",
            "end_date": "9/1/15"
        },
        {
            "proj_num": "Project 2",
            "city_cost": "high",
            "start_date": "9/2/15",
            "end_date": "9/6/15"
        },
        {
            "proj_num": "Project 3",
            "city_cost": "low",
            "start_date": "9/6/15",
            "end_date": "9/8/15"
        }
    ],
}
```
You can pass any JSON file with data fitting this criteria can be passed in as an argument to the command line:

```
python3 main.py sample-sets.json
```