
# get daily hours
def collect_weekly_hours():
    hrs_list = []
    for day in range(1,6):
        while True:
                user_input = input(f"Eneter hours worked for Day {day}: ")
        
                if user_input == "":
                    print("Error: Input cannot be empty. Please eneter a number")
                    continue
        
                test_nums = user_input
                if test_nums.startswith('-'):
                    test_nums = test_nums[1:]
        
                if test_nums.count(".") <=1:
                    test_nums = test_nums.replace(".", "", 1)
        
                if test_nums.isdigit():
                    hours = float(user_input)
                    if 0 <= hours <= 24:
                        hrs_list.append(hours) 
                        break
                    else:
                        print( "Error: Hours must be between 0 and 24" )
                else: print("Error: Please enter a valid number")
        
    return hrs_list

# calc total hours    
def calculate_totals(hrs_list):
    total_hours = 0.0
    for hrs in hrs_list:
        total_hours = total_hours + hrs
    return total_hours

# calc average
def calculate_average(hrs_list, total_hours):
    average_hours = total_hours / len(hrs_list)
    return average_hours

# max hours loop    
def find_max_hours(hrs_list):
    max_hours = hrs_list [0]
    for hrs in hrs_list:
        if hrs > max_hours:
            max_hours = hrs
    return max_hours

# find highest day loop
def find_highest_days(hrs_list, max_hours):
    highest_days = []
    for h in range(len(hrs_list)):
        if hrs_list [h] == max_hours:
            highest_days = highest_days + [str(h + 1)]
    return highest_days

# find slacker loop
def find_under_target(hrs_list):
    normal_day = 7.0
    under_target = []
    for h in range(len(hrs_list)):
        if hrs_list[h] < normal_day:
            under_target = under_target + [(h + 1, hrs_list[h])]
    return under_target

# output results
def display_summary(total_hours, average_hours, max_hours, highest_days, under_target):
    normal_day= 7.0
    print("\n" + "="*36)
    print('       ANS Timesheet Summary       ')
    print("="*36)
    print(f"Toatl Hours Worked: {total_hours:.2f} hrs")
    print(f"Average Daily Hours: {average_hours:.2f} hrs/day")

  
    day_hrs = ", Day".join(highest_days)
    print(f"Highest Day(s): Day {day_hrs} with {max_hours:.2f} hours")

    print("-" *36)
    print(f"Days with slacker hours or < ({normal_day} hrs)")
    if len(under_target) > 0:
        for item in under_target:
            day_num = item[0]
            hrs1 = item[1]
            print(f" - Day {day_num}: {hrs1} hrs")
        print("LET'S UP THOSE NUMBERS!")
    else:
        print(" - NONE! A true ANS champ!")
    print('='*36)
    
def main():
    print("Welcome to ANS Contracting Weekly Hour Tracking App")
    
    hrs_list = collect_weekly_hours()

    total_hours = calculate_totals(hrs_list)

    average_hours = calculate_average(hrs_list, total_hours)

    max_hours = find_max_hours(hrs_list)

    highest_days = find_highest_days(hrs_list, max_hours)

    under_target = find_under_target(hrs_list)

    display_summary(total_hours, average_hours, max_hours, highest_days, under_target)
    
main()
