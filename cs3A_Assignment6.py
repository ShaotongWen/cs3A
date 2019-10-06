""" Assignment Six: Bubble sort using recursion - Shaotong Wen """


def new_file(dataset):
    """ to be implemented """
    print("New File Function Called")


def choose_units():
    """ to be implemented """
    print("Choose Units Function Called")


def change_filter(sensor_list, active_sensors):
    """ to be implemented """
    print("Change Filter Function Called")


def print_summary_statistics(dataset, active_sensors):
    """ to be implemented """
    print("Summary Statistics Function Called")


def print_temp_by_day_time(dataset, active_sensors):
    """ to be implemented """
    print("Print Temp by Day/Time Function Called")


def print_histogram(dataset, active_sensors):
    """ to be implemented """
    print("Print Histogram Function Called")


def print_menu():
    """ print the main menu """
    print()
    print("Main Menu")
    print("---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")
    print()


def print_header():
    """ Print a friendly header for our project. """
    print("STEM Center Temperature Project")
    print("Shaotong Wen")


def convert_units(celsius_value, units):
    """ convert given Celsius temp to Fahrenheit or Kelvin"""
    if units == 0:
        return celsius_value
    if units == 1:
        return celsius_value * 1.8 + 32
    return celsius_value + 273.15


def test_sensor_setup(sensor_list, active_sensors):

    print("Testing sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list content:")
    rooms_list = [i[0] for i in sensor_list]
    descriptions_list = [i[1] for i in sensor_list]
    if "4213" not in rooms_list or "Out" not in rooms_list:
        print("Fail - something is wrong with the room numbers")
    elif "Foundations Lab" not in descriptions_list:
        print("Fail - something is wrong with room descriptions")
    else:
        print("Pass")

    print("Testing active_sensors length:")
    if len(active_sensors) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing active_sensors content:")
    if sum(active_sensors) == 20:
        print("Pass")
    else:
        print("Fail")


def recursive_sort(sensor_list, key):
    """Bubble sort using recursion"""
    new_list = sensor_list.copy()
    for i, num in enumerate(new_list):
        # try:
            if key == 0:
                if new_list[i + 1][0] < num[0]:
                    new_list[i] = sensor_list[i + 1]
                    new_list[i + 1] = num
                    recursive_sort(new_list, key)
            if key == 1:
                if new_list[i + 1][1] < num[1]:
                    new_list[i] = new_list[i + 1]
                    new_list[i + 1] = num
                    recursive_sort(new_list, key)
        # except IndexError:
        #     # pass
            return new_list


def main():

    sensor_list = [
        ("4213", "STEM Center", 0),
        ("4201", "Foundations Lab", 1),
        ("4204", "CS Lab", 2),
        ("4218", "Workshop Room", 3),
        ("4205", "Tiled Room", 4),
        ("Out", "Outside", 10)]

    print(sensor_list)
    print(recursive_sort(sensor_list, 0))
    print(recursive_sort(sensor_list, 1))
    print(sensor_list)

    # Two ways to set up sensor_list
    # I prefer the second for readability
    # active_sensors = [sensor_list[i][2] for i in range(len(sensor_list))]
    # active_sensors = [sensor[2] for sensor in sensor_list]

    # test_sensor_setup(sensor_list, active_sensors)

    print_header()

    while True:
        print_menu()
        try:
            choice = int(input("What is your choice? "))
        except ValueError:
            print("*** Please enter a number only ***")
        else:
            if choice == 1:
                new_file(None)
            elif choice == 2:
                choose_units()
            elif choice == 3:
                change_filter(None, None)
            elif choice == 4:
                print_summary_statistics(None, None)
            elif choice == 5:
                print_temp_by_day_time(None, None)
            elif choice == 6:
                print_histogram(None, None)
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid Choice")


if __name__ == "__main__":
    main()


""" ----- SAMPLE RUN -----

[('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205
', 'Tiled Room', 4), ('Out', 'Outside', 10)]
[('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 
'Workshop Room', 3), ('Out', 'Outside', 10)]
[('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('Out', '
Outside', 10), ('4218', 'Workshop Room', 3)]
[('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205
', 'Tiled Room', 4), ('Out', 'Outside', 10)]
STEM Center Temperature Project
Shaotong Wen

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 

"""