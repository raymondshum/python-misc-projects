import re
from functools import reduce

def add_two_times(time1, time2):
    if not time1:
        return time2
    elif not time2:
        return time1

    time1_hours, time1_minutes = [int(num) for num in time1.split(".")]
    time2_hours, time2_minutes = [int(num) for num in time2.split(".")]

    carryover_hours = int((time1_minutes + time2_minutes) / 60)
    new_minutes = (time1_minutes + time2_minutes) % 60
    new_hours = time1_hours + time2_hours + carryover_hours

    return ".".join((str(new_hours), str(new_minutes)))

def main():
    user_input = ""
    time_values = []

    # get time values
    while user_input != "stop":
        user_input = input("Please enter time value {h.mm} or \"stop\": ")
        format_is_correct = re.search("^[0-9].[0-9][0-9]$",user_input)

        if format_is_correct:
            print(f"Added: {user_input}")
            time_values.append(user_input.lower().strip()) 
        
    print("Total time: ", reduce(add_two_times, time_values))

if __name__ == "__main__":
    main()