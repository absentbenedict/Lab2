def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")
    return


    
def calc_average(floatlist):
    average = sum(floatlist) / len(floatlist)
    print("Average:", average)
    return average

def get_user_input():
    x=input()
    splitlist=x.split(',')
    floatlist = [float(num) for num in splitlist]
    print(floatlist)
    return floatlist
    
def find_min_max(floatlist):
    if len(floatlist) == 0:  # Check if the list is empty
        print("No numbers provided.")
        return None, None
    min_temp = min(floatlist)
    max_temp = max(floatlist)
    print("Minimum Temperature:", min_temp)
    print("Maximum Temperature:", max_temp)
    return min_temp, max_temp


def sort_temperature(floatlist):
    sorted_list = sorted(floatlist)
    print("Sorted Temperatures:", sorted_list)
    return sorted_list

def calc_median_temperature(floatlist):
    if len(floatlist) == 0:  # Check if the list is empty
        print("No numbers provided.")
        return None
    sorted_list = sorted(floatlist)  # Sort the list
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:  # If even number of elements
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:  # If odd number of elements
        median = sorted_list[mid]
    print("Median Temperature:", median)
    return median

display_main_menu()
floatlist = get_user_input()
calc_average(floatlist)
find_min_max(floatlist)
calc_median_temperature(floatlist)