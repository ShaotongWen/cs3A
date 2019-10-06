""" Assignment 10: Print Summary Statistics - Shaotong Wen """


class TempDataset:
    mum_objects = 0
    MIN_LEN = 3
    MAX_LEN = 20

    def __init__(self):
        """ initialize instance variables """
        self._data_set = []
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

        for next_line in my_file:
            my_tuple = tuple(next_line.split(","))
            if my_tuple[0].isdigit() and my_tuple[3] == 'TEMP':
                time_of_day = math.floor(float(my_tuple[1]) * 24)
                temp = my_tuple[4].rstrip()
                new_tuple = (int(my_tuple[0]), time_of_day, int(my_tuple[2]), float(temp))
                self._data_set.append(new_tuple)
        return True

    def get_summary_statistics(self, active_sensors):
        """The method gets the summary of the statistics."""
        print(active_sensors)
        print(len(self._data_set))
        if self._data_set is None or active_sensors == []:
            return None
        else:
            temperature_data = []
            temperature_sum = 0.00
            temperature_average = 0.00
            for i in self._data_set:
                for k in active_sensors:
                    if i[2] == k and i[0]:
                        temperature_data.append(i[3])
                        temperature_sum += i[3]
            if len(temperature_data) > 0:
                temperature_average = temperature_sum/float(len(temperature_data))
                print(temperature_sum, len(temperature_data))
                def_tup = (min(temperature_data), max(temperature_data), temperature_average)
            else:
                def_tup = (0, 0, 0)
            return def_tup

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        """The method gets the average temperature."""
        # Now we also want it to return None if there are no sensors
        # active in active_sensors or if the active sensors
        # have no readings (you can do both in one statement!).
        if self._data_set is None or active_sensors == []:
            return None
        else:
            # temperature_data = []
            # temperature_sum = 0.00
            # temperature_average = 0.00
            # for i in self._data_set:
            #     for k in active_sensors:
            #         if i[2] == k and i[0] == day and i[1] == time:
            #             temperature_data.append(i[3])
            #             temperature_sum += i[3]
            # if len(temperature_data) > 0:
            #     temperature_average = temperature_sum/float(len(temperature_data))
            # return temperature_average
            temp_data = [k[3] for k in self._data_set if day == k[0] and time == k[1] and k[2] in
                         active_sensors]
            if len(temp_data) > 0:
                return sum(temp_data) / len(temp_data)
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


# create a constant
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}
current_unit = 0


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

# REPORT what the current units are
# GIVE A MENU of the available units


def choose_units(current_set):
    global current_unit
    print(f"Current units in {UNITS[current_unit][0]}")

    while True:
        for index in range(len(UNITS)):
            print(f"{index} ---- {UNITS[index][0]}")
        try:
            print("Choose new units:")
            new_unit = int(input("Which unit?"))
        except ValueError:
            print("*** Please enter a number only ***")
        else:
            if 0 <= new_unit <= 3:
                print('Bingo')
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
        print(current_set.get_summary_statistics(active_sensors))
        print(current_set.get_avg_temperature_day_time(active_sensors, 5, 7))
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