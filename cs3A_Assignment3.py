""" Assignment Three: Temperature Conversions - Shaotong Wen """


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


def main():
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

What is your choice? 1
New File Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 2
New Choose Units Called

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
Change Filter Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 4
Summary Statistics Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 5
Print Temp by Day/Time Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 6
Print Histogram Function Called

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 10
Invalid Choice 

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? b
*** Please enter a number only ***

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? -1
Invalid Choice 

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 7
Thank you for using the STEM Center Temperature Project 

Process finished with exit code 0

"""