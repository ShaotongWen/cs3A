""" Assignment 9: File Import - Shaotong Wen """


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
        """The method gets the summary of the statistics."""
        if self._data_set is None:
            return None
        else:
            def_tup = (0, 0, 0)
            return def_tup

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """The method gets the average temperature."""
        if self._data_set is None:
            return None
        else:
            return 0

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


def choose_units():
    print("Choose Units Function Called")


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
    print("Summary Statistics Function Called")


def print_temp_by_day_time(dataset, active_sensors):
    print("Print Temp by Day/Time Function Called")


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
                choose_units()
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
Please enter the filename of the new dataset:test.csv
It is unable to load a file.

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
Please provide a 3 to 20 character name for the dataset:sw
The name you typed was bad! Please provide a 3 to 20 character name for the dataset:temperature

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