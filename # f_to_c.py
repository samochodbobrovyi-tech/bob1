# f_to_c.py
# Simple Fahrenheit to Celsius converter
# Author: Bohdan Romanchenko
# License: MIT License

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("=== Fahrenheit to Celsius Converter ===")
    try:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c:.2f}°C")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
