CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    """Prompts the user for temperature conversion and performs the operation."""
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input(
                "Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                unit_symbol = "°C"
                converted_unit_symbol = "°F"
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                unit_symbol = "°F"
                converted_unit_symbol = "°C"
            else:
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            print(
                f"{temperature:.1f}{unit_symbol} is {converted_temp:.1f}{converted_unit_symbol}")
            break
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
