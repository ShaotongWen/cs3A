""" Assignment 11: Print Summary Statistics - Shaotong Wen """


class TempDataset:
    mum_objects = 0
    MIN_LEN = 3
    MAX_LEN = 20

    def __init__(self):
        """ initialize instance variables """
        self._data_set = None
        self._name = "Unnamed"
        TempDataset.mum_objects += 1

    @property
    def name(self):
        """The method simply returns the name of the dataset."""
        return self._name

    @name.setter
    def name(self, the_name):
        """The method replaces the default name of the dataset."""
        if (len(the_name) < TempDataset.MIN_LEN
           or len(the_name) > TempDataset.MAX_LEN):
            raise ValueError
        self._name = the_name

    def dataset(self):
        return self._data_set

    def process_file(self, filename):
        """The method is used to process a file."""
        import math
        try:
            my_file = open(filename, "r")
        except FileNotFoundError:
            return False
        self._data_set = []
        for next_line in my_file:
            my_tuple = tuple(next_line.split(","))
            if my_tuple[3] == 'TEMP':
                time_of_day = math.floor(float(my_tuple[1]) * 24)
                temp = my_tuple[4].rstrip()
                new_tuple = (int(my_tuple[0]), time_of_day, int(my_tuple[2]), float(temp))
                self._data_set.append(new_tuple)
        return True

    def get_summary_statistics(self, active_sensors):
        """The method returns the summary of temperature statistics."""
        if self._data_set is None or active_sensors == []:
            return None
        else:
            temp_data = [k[3] for k in self._data_set if k[2] in active_sensors]
            if len(temp_data) > 0:
                min_temp = convert_units(min(temp_data), current_unit)
                max_temp = convert_units(max(temp_data), current_unit)
                ave_temp = convert_units(float(sum(temp_data)) / float(len(temp_data)), current_unit)
                def_tup = (round(min_temp, 2), round(max_temp, 2), round(ave_temp, 2))
            else:
                def_tup = (0, 0, 0)
            return def_tup

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """The method returns the average temperature of the loaded data set."""
        if self._data_set is None or active_sensors == []:
            return None
        else:
            temp_data = [k[3] for k in self._data_set if day == k[0] and time == k[1] and k[2] in
                         active_sensors]
            if len(temp_data) > 0:
                return round(convert_units((sum(temp_data) / len(temp_data)), current_unit), 1)
            else:
                return None

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        """The method gets the number of temps."""
        if self._data_set is None:
            return None
        else:
            return 0

    def get_loaded_temps(self):
        """The method gets the loaded temps."""
        # The data loaded successfully as long as instance variable _data_set is updated.
        if self._data_set is None:
            return None
        else:
            return int(len(self._data_set))

    @classmethod
    def get_num_objects(cls):
        """The method gets the number of objects created"""
        return cls.mum_objects

    @property
    def data_set(self):
        return self._data_set


# create a constant
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}
current_unit = 0
DAYS = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT"
}

HOURS = {
    0: "Mid-1AM  ",
    1: "1AM-2AM  ",
    2: "2AM-3AM  ",
    3: "3AM-4AM  ",
    4: "4AM-5AM  ",
    5: "5AM-6AM  ",
    6: "6AM-7AM  ",
    7: "7AM-8AM  ",
    8: "8AM-9AM  ",
    9: "9AM-10AM ",
    10: "10AM-11AM",
    11: "11AM-NOON",
    12: "NOON-1PM ",
    13: "1PM-2PM  ",
    14: "2PM-3PM  ",
    15: "3PM-4PM  ",
    16: "4PM-5PM  ",
    17: "5PM-6PM  ",
    18: "6PM-7PM  ",
    19: "7PM-8PM  ",
    20: "8PM-9PM  ",
    21: "9PM-10PM ",
    22: "10PM-11PM",
    23: "11PM-MID ",
}


def print_header():
    """ print an opening message """
    print("STEM Center Temperature Project")
    print("Shaotong Wen")


def recursive_sort(list_to_sort, key=0):
    """ sort a list of tuples on the given key """
    length = len(list_to_sort)
    if length <= 1:
        return list_to_sort
    swaplist = list_to_sort.copy()
    for i in range(0, length - 1):
        if swaplist[i][key] > swaplist[i + 1][key]:
            (swaplist[i], swaplist[i + 1]) = \
                (swaplist[i + 1], swaplist[i])
    return recursive_sort(swaplist[0:length - 1], key) \
           + swaplist[length - 1:length]


def new_file(dataset):
    import sys
    """
    This function asks for a filename and then use process_file() to load the data.
    If loading the data succeeds, ask for a name for the data.
    """
    filename = input("Please enter the filename of the new dataset:")
    if dataset.process_file(filename):
        print(f"Loaded {dataset.get_loaded_temps()} samples")
        new_name = input("Please provide a 3 to 20 character name for the dataset:")
        while True:
            try:
                dataset.name = new_name
                break
            except ValueError:
                new_name = input("The name you typed was bad! "
                                 "Please provide a 3 to 20 character name for the dataset:")
    else:
        print('It is unable to load a file.')


def choose_units(current_set):
    """The method reports what the current units are and changes current_units to the user's selection"""
    global current_unit
    print(f"Current units in {UNITS[current_unit][0]}")

    while True:
        for item in UNITS:
            print(f"{item} - {UNITS[item][0]}")
        try:
            print("Choose new units:")
            new_unit = int(input("Which unit?"))
        except ValueError:
            print("*** Please enter a number only ***")
        else:
            if new_unit in [item for item in UNITS]:
                current_unit = new_unit
                break
            else:
                print('Please choose a unit from the list')


def print_filter(sensor_list, active_sensors):
    """ print the list of sensors, noting those that are active """
    for sensor in sensor_list:
        print(sensor[0], sensor[1], sep=': ', end='')
        print(' [ACTIVE]') if sensor[2] in active_sensors else print('')


def change_filter(sensor_list, active_sensors):
    """ allow the user to modify which sensors are active """
    sensors = {sensor[0]: sensor[2] for sensor in sensor_list}
    while True:
        print()
        print_filter(sensor_list, active_sensors)
        print()
        print(f"Type the sensor to toggle (e.g. {sensor_list[0][0]})"
              f" or x to end", end=' ')
        choice = input()
        if choice == "x":
            break
        if choice in sensors:
            if sensors[choice] in active_sensors:
                active_sensors.remove(sensors[choice])
            else:
                active_sensors.append(sensors[choice])
        else:
            print("Invalid Sensor")


def print_summary_statistics(dataset, active_sensors):
    """This method prints the summary of temperature statistics."""
    temp_statistics = dataset.get_summary_statistics(active_sensors)
    if temp_statistics is None:
        print('Please load data file and make sure at least one sensor is active')
    else:
        print(f"Summary statistics for {dataset.name}")
        print(f"Minimum Temperature:{temp_statistics[0]} {UNITS[current_unit][1]}")
        print(f"Maximum Temperature:{temp_statistics[1]} {UNITS[current_unit][1]}")
        print(f"Average Temperature:{temp_statistics[2]} {UNITS[current_unit][1]}")


def print_temp_by_day_time(dataset, active_sensors):
    """ print a table that shows the average temperature in our labs by day of week and hour of day"""
    if dataset.get_loaded_temps() is None:
        print('file not loaded')
    else:
        print(f"Average Temperatures for {dataset.name}")
        print(f"Units are in {UNITS[current_unit][0]}")

        a = [dataset.get_avg_temperature_day_time(active_sensors, j, k)
             for k in range(len(HOURS)) for j in range(len(DAYS))]

        if not a:
            b = [[' ---'] * len(DAYS) for i in range(len(HOURS))]
        else:
            b = [a[i:i + len(DAYS)] for i in range(0, len(a), len(DAYS))]

        print("         ", end="")
        for c in DAYS:
            print(f"    {DAYS[c]}", end="")
        print()

        for d in range(len(b)):
            label = HOURS[d]
            print(label, end="")

            for e in b[d]:
                print(f"   {e}", end="")
            print()


def print_histogram(dataset, active_sensors):
    print("Print Histogram Function Called")


def print_menu():
    """ Print the main menu """
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


def convert_units(celsius_value, units):
    """ convert celsius to celsius, Fahrenheit or Kelvin """
    if units == 0:
        return celsius_value
    if units == 1:
        return celsius_value * 1.8 + 32
    return celsius_value + 273.15


def main():
    sensor_list = [
        ("4213", "STEM Center", 0),
        ("4201", "Foundations Lab", 1),
        ("4204", "CS Lab", 2),
        ("4218", "Workshop Room", 3),
        ("4205", "Tiled Room", 4),
        ("Out", "Outside", 10)]

    active_sensors = [sensor[2] for sensor in sensor_list]
    sensor_list = recursive_sort(sensor_list, 0)
    current_set = TempDataset()
    print_header()
    while True:
        print_menu()
        try:
            choice = int(input("What is your choice? "))
        except ValueError:
            print("*** Please enter a number only ***")
        else:
            if choice == 1:
                new_file(current_set)
            elif choice == 2:
                choose_units(current_set)
            elif choice == 3:
                change_filter(sensor_list, active_sensors)
            elif choice == 4:
                print_summary_statistics(current_set, active_sensors)
            elif choice == 5:
                print_temp_by_day_time(current_set, active_sensors)
            elif choice == 6:
                print_histogram(current_set, active_sensors)
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Invalid Choice")


if __name__ == "__main__":
    main()


""" ----- SAMPLE RUN -----
/Users/wenshaotong/PycharmProjects/oop/venv/bin/python /Users/wenshaotong/PycharmProjects/oop/Assignment11.py
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
Please enter the filename of the new dataset:Temperatures2017-08-06.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset:Test week

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
Current units in Celsius
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Choose new units:
Which unit?1

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

4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4201

4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4204

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4205

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end Out

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside

Type the sensor to toggle (e.g. 4201) or x to end x

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
Average Temperatures for Test week
Units are in Fahrenheit
             SUN    MON    TUE    WED    THU    FRI    SAT
Mid-1AM     68.8   68.4   72.7   71.3   70.6   70.7   66.8
1AM-2AM     69.0   68.3   72.5   71.1   70.3   70.5   66.9
2AM-3AM     69.1   68.3   72.3   70.9   70.0   70.4   67.0
3AM-4AM     69.2   68.1   72.2   70.8   69.8   70.3   67.0
4AM-5AM     69.2   68.1   72.1   70.6   69.7   70.1   67.1
5AM-6AM     69.2   68.0   72.1   70.5   69.6   70.0   67.1
6AM-7AM     68.8   67.9   72.1   70.1   69.4   69.6   67.1
7AM-8AM     68.1   68.1   71.8   70.0   69.5   69.2   67.1
8AM-9AM     67.4   68.1   71.1   69.5   69.7   68.3   67.1
9AM-10AM    67.3   69.1   71.5   69.4   70.6   67.1   67.2
10AM-11AM   67.1   70.4   72.3   69.9   71.5   66.6   67.2
11AM-NOON   66.9   70.9   73.2   70.4   72.2   66.6   66.6
NOON-1PM    66.8   71.2   73.1   71.3   72.1   66.3   65.9
1PM-2PM     66.7   71.9   73.6   72.3   71.9   66.1   65.5
2PM-3PM     66.9   72.8   74.3   73.1   72.3   66.1   65.2
3PM-4PM     66.7   73.3   74.7   74.0   72.7   66.1   65.0
4PM-5PM     66.7   73.8   75.1   74.4   73.4   66.0   64.9
5PM-6PM     66.7   74.2   75.7   74.9   74.0   66.0   64.9
6PM-7PM     66.7   73.5   75.1   74.6   73.5   65.8   64.8
7PM-8PM     67.2   73.4   74.0   73.4   72.5   65.7   64.8
8PM-9PM     67.8   73.4   73.0   72.6   71.7   65.4   64.7
9PM-10PM    68.1   73.3   72.2   71.7   71.1   65.5   64.9
10PM-11PM   68.3   73.2   71.8   71.3   70.9   66.3   65.5
11PM-MID    68.6   73.0   71.5   70.9   70.8   66.6   65.7

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