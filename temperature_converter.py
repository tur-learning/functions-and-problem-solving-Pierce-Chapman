# Convert Celsius to Fahrenheit using the formula: F = C * (9/5) + 32
def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")