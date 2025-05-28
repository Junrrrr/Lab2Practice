print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")  

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    userinput = input()
    input_list = userinput.split(",")
    print(input_list)
    return input_list

def calc_average(strlist):
    print("calc_average") 
    total = 0.0  
    for i in strlist:
        total = total + len(strlist)
    average = total / len(strlist)
    return average

def find_min_max(strlist):
    print("find_min_max")
    floatlist = []
    for i in strlist:
        floatlist.append(float(i))

    floatlist.sort()
    max = floatlist[-1]
    min = floatlist[0]
    print("Max = ", max)
    print("Min = ", min)
    return(min, max)


def sort_temperature(input_list):
    print("sort_temperature")
    input_list.sort()

def calc_median_temperature(input_list):
    print("calc_median_temperature")
    if len(input_list) % 2 == 1:
        median = input_list(len(input_list) // 2)

    else:
        median = (input_list[cnt//2] + input_list[cnt//2-1])/2
    print("Median = ", median)



def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)
    sort_temperature(floatlist)
    print("After sorting = ", floatlist)
    calc_median_temperature(floatlist)
    
if __name__ == "__main__":
    main()
