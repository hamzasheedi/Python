def main():
    print("Convert Your Fahrenheit Temperature into Celsius.")
    
    # Ask user to enter temperature in Fahrenheit
    degrees_fahrenheit = float(input("Write Temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius using the formula
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    
    # Print the result
    print(f"{degrees_fahrenheit} °F is equal to {degrees_celsius:.2f} °C")


# Boilerplate to call main function
if __name__ == '__main__':
    main()
