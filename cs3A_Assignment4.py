""" Assignment Four: Temperature Conversions - Shaotong Wen """


def print_header():
    """ Print the project name and my name. """
    print("STEM Center Temperature Project")
    print("Shaotong Wen")


def convert_units(celsius_value, units):
    """ convert given Celsius temp to Fahrenheit or Kelvin"""
    if units == 0:
        return celsius_value
    if units == 1:
        return celsius_value * 1.8 + 32
    return celsius_value + 273.15


def print_menu():
    """ Print the menu. """
    print("Main Menu")
    print("---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")


def new_file(dataset):
    print("New File Function Called")


def choose_units():
    print("New Choose Units Called")


def change_filter(sensor_list, active_sensors):
    print("Change Filter Function Called")


def print_summary_statistics(dataset, active_sensors):
    print("Summary Statistics Function Called")


def print_temp_by_day_time(dataset, active_sensors):
    print("Print Temp by Day/Time Function Called")


def pprint_histogram(dataset, active_sensors) :
    print("Print Histogram Function Called")


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
    sensor_list = \
        [("4213", "STEM Center", 0),
         ("4201", "Foundations Lab", 1),
         ("4204", "CS Lab", 2),
         ("4218", "Workshop Room", 3),
         ("4205", "Tiled Room", 4),
         ("Out", "Outside", 10)]

    active_sensors = []
    for i in range(0, len(sensor_list)):
        active_sensors.append(sensor_list[i][2])

    test_sensor_setup(sensor_list, active_sensors)

    print_header()
    while True:
        try:
            print()
            print_menu()
            print()
            user_choice = int(input("What is your choice? "))
        except ValueError:
            print("*** Please enter a number only ***")
            continue

        if user_choice not in range(1, 8):
            print("Invalid Choice ")
        else:
            if user_choice == 1:
                new_file(None)
            if user_choice == 2:
                choose_units()
            if user_choice == 3:
                change_filter(None, None)
            if user_choice == 4:
                print_summary_statistics(None, None)
            if user_choice == 5:
                print_temp_by_day_time(None, None)
            if user_choice == 6:
                pprint_histogram(None, None)
            if user_choice == 7:
                print("Thank you for using the STEM Center Temperature Project ")
                break


if __name__ == "__main__":
    main()


""" ----- SAMPLE RUN -----

Testing sensor_list length:
Pass
Testing sensor_list content:
Pass
Testing active_sensors length:
Pass
Testing active_sensors content:
Pass
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