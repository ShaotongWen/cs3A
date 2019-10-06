""" Assignment Two: Temperature Conversions - Shaotong Wen
"""


def print_header():
    """Print the project name and my name."""
    print("STEM Center Temperature Project")
    print("Shaotong Wen")


def convert_units(celsius_value, units):
    """ convert two arguments passed """
    if units == 0:
        return celsius_value
    if units == 1:
        return float(celsius_value) * (9/5) + 32
    if units == 2:
        return float(celsius_value) + 273.15


def main():
    print_header()
    # prepare a prompt for the user
    str_prompt = "Please enter a temperature in degrees Celsius:"

    # show user the prompt and get the user response
    str_user_input = input(str_prompt)

    # call the function and get the temperatures converted
    convert_units(str_user_input, 0)
    fahrenheit = convert_units(str_user_input, 1)
    kelvin = convert_units(str_user_input, 2)

    print(f"That's {str(fahrenheit)} degrees Fahrenheit and \n{str(kelvin)} Kelvin")


if __name__ == "__main__":
    main()


""" ----- SAMPLE RUN -----

STEM Center Temperature Project
Shaotong Wen
Please enter a temperature in degrees Celsius:30
That's 86.0 degrees Fahrenheit and 
303.15 Kelvin

"""