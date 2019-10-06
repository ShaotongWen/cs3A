""" Assignment Eight: Dataset Class - Shaotong Wen """


class TempDataset:
    """ initialize instance variables """

    mum_objects = 0

    def __init__(self):
        self._data_set = None
        self.data_set_name = "Unnamed"

        TempDataset.mum_objects += 1

    @property
    def name(self):
        """The method simply returns the name of the dataset."""
        return self.data_set_name

    @name.setter
    def name(self, the_name):
        """The method replaces the default name of the dataset."""
        if type(the_name) != str or the_name.isprintable() is False or len(the_name) < 3 or len(the_name) > 20:
            raise ValueError
        self.data_set_name = the_name

    def process_file(self, filename):
        """The method is used to process a file."""
        return False

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
        if self._data_set is None:
            return None
        else:
            return 0

    @classmethod
    def get_num_objects(cls):
        """The method gets the number of objects created"""
        return cls.mum_objects


def main():

    current_set = TempDataset()

    print("First test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 1:
        print("Success")
    else:
        print("Fail")

    second_set = TempDataset()

    print("Second test of get_num_objects: ", end='')

    if TempDataset.get_num_objects() == 2:
        print("Success")
    else:
        print("Fail")

    print("Testing get_name and set_name: ")

    print("- Default Name:", end='')

    if current_set.name == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("- Try setting a name too short: ", end='')

    try:
        current_set.name = "to"
        print("Fail")
    except ValueError:
        print("Success")

    print("- Try setting a name too long: ", end='')

    try:
        current_set.name = "supercalifragilisticexpialidocious"
        print("Fail")
    except ValueError:
        print("Success")

    print("- Try setting a name just right (Goldilocks): ", end='')

    try:
        current_set.name = "New Name"
        if current_set.name == "New Name":
            print("Success")
        else:
            print("Fail")
    except ValueError:
        print("Fail")

    print("- Make sure we didn't touch the other object: ", end='')
    if second_set.name == "Unnamed":
        print("Success")
    else:
        print("Fail")

    print("Testing get_avg_temperature_day_time: ", end='')
    if current_set.get_avg_temperature_day_time(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_num_temps: ", end='')
    if current_set.get_num_temps(None, 0, 0) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_loaded_temps: ", end='')
    if current_set.get_loaded_temps() is None:
        print("Success")
    else:
        print("Fail")

    print("Testing get_summary_statistics: ", end='')
    if current_set.get_summary_statistics(None) is None:
        print("Success")
    else:
        print("Fail")

    print("Testing process_file: ", end='')
    if current_set.process_file(None) is False:
        print("Success")
    else:
        print("Fail")


if __name__ == "__main__":
    main()

""" ----- SAMPLE RUN -----

First test of get_num_objects: Success
Second test of get_num_objects: Success
Testing get_name and set_name: 
- Default Name:Success
- Try setting a name too short: Success
- Try setting a name too long: Success
- Try setting a name just right (Goldilocks): Success
- Make sure we didn't touch the other object: Success
Testing get_avg_temperature_day_time: Success
Testing get_num_temps: Success
Testing get_loaded_temps: Success
Testing get_summary_statistics: Success
Testing process_file: Success

"""
