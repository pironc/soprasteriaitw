##
## SOPRA STERIA ITW
## EVEN OR ODD
##


import random


# Function to process the paycheck based on the worked hours, pay rate, handling overtime work with a 50% added pay
def process_paycheck(worked_hours, payrate):
    regular_work_hours = 40
    overtime_multiplier = 1.50
    paid_amount = 0.00

    if worked_hours > 40:
        overwork_time = (worked_hours - regular_work_hours)
        paid_amount = (40 * payrate) + (overwork_time * (overtime_multiplier * payrate))
    else:
        paid_amount = worked_hours * payrate
    paid_amount = round(paid_amount, 2)

    print(f"Paid amount: {paid_amount}")
    return (0)


# Function to get the hours worked by an employee, from 20 to 65 hours with a step of 5
def read_worked_hours():
    worked_hours = random.randrange(20, 65, 5)
    return (worked_hours)


# Function to get a pay rate from 14 to 26 with a randomized floating point value for a more realistic outcome
def read_payrate():
    euros = random.randint(14, 26)
    cents = random.random()

    payrate = round((euros + cents), 2)
    return (payrate)


# Main function to run the program and get default variables to use in the program functions
def main():
    worked_hours = read_worked_hours()
    payrate = read_payrate()

    print(f"Worked hours: {worked_hours}")
    print(f"Pay rate: {payrate}")
    ret = process_paycheck(worked_hours, payrate)

    return (ret)

main()