""" Assignment Six - Shaotong Wen """


def recursive_sort(list_to_sort, key=0):
    """ sort a list of tuples on the given key """
    swap = False
    length = len(list_to_sort)
    if length <= 1:
        return list_to_sort
    for i in range(0, length - 1):
        if list_to_sort[i][key] > list_to_sort[i + 1][key]:
            (list_to_sort[i], list_to_sort[i + 1]) = \
                (list_to_sort[i + 1], list_to_sort[i])
            swap = True
    if swap is False:
        return list_to_sort
    return recursive_sort(list_to_sort[0:length-1], key) + list_to_sort[length-1:length]


def print_filter(sensor_list, active_sensors):
    print()
    for k in range(len(sensor_list)):
        for j in range(len(active_sensors)):
            if sensor_list[k][2] == active_sensors[j]:
                print(f"{sensor_list[k][0]}: {sensor_list[k][1]} {active_sensors[j]} [ACTIVE]")


def change_filter(sensor_list, active_sensors):
    """ toggling the sensors when use enters number"""
    # print("Change Filter Function Called")
    sensors = {}
    for i in range(len(sensor_list)):
        sensors[sensor_list[i][0]] = sensor_list[i][2]


def new_file(dataset):
    """ to be implemented """
    print("New File Function Called")


def choose_units():
    """ to be implemented """
    print("Choose Units Function Called")


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


def main():

    sensor_list = [
        ("4213", "STEM Center", 0),
        ("4201", "Foundations Lab", 1),
        ("4204", "CS Lab", 2),
        ("4218", "Workshop Room", 3),
        ("4205", "Tiled Room", 4),
        ("Out", "Outside", 10)]

    # Two ways to set up sensor_list
    # I prefer the second for readability
    # active_sensors = [sensor_list[i][2] for i in range(len(sensor_list))]

    sensor_list = recursive_sort(sensor_list)
    active_sensors = [sensor[2] for sensor in sensor_list]
    print(print_header())
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
                print_filter(sensor_list, active_sensors)
                change_filter(sensor_list, active_sensors)
                print()
                while True:
                    input_sensor = str(input('Type the sensor number to toggle (e.g.4201) or x to end:'))
                    if input_sensor == 'x':
                        exit
                    else:
                        print("Invalid Sensor")
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
STEM Center Temperature Project
Shaotong Wen
None

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 3

4201: Foundations Lab 1 [ACTIVE]
4204: CS Lab 2 [ACTIVE]
4205: Tiled Room 4 [ACTIVE]
4213: STEM Center 0 [ACTIVE]
4218: Workshop Room 3 [ACTIVE]
Out: Outside 10 [ACTIVE]

Type the sensor number to toggle (e.g.4201) or x to end:4204
Invalid Sensor
Type the sensor number to toggle (e.g.4201) or x to end:x
Type the sensor number to toggle (e.g.4201) or x to end:
"""