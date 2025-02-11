print("main script is running...")

from bmr_calculator import calculate_bmr, chocolate_bars_needed
from temperature_converter import celsius_to_fahrenheit
from time_converter import seconds_to_hms

# Main function that executes the BMR calculation, temperature conversion, and time conversion.
def main(): 
    
    # BMR Calculation
    print("\n--- BMR Calculation ---")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in cm:"))
    age = int(input("Enter age in years:"))

    # Calculate BMR for men and women
    bmr_m, bmr_w = calculate_bmr(weight, height, age)

    # Calculate how many chocolate bars are needed to maintain the BMR
    bars_m = chocolate_bars_needed(bmr_m)
    bars_w = chocolate_bars_needed(bmr_w)

    # Display results
    print(f"BMR for men: {bmr_m:.2f} calories/day")
    print(f"BMR for women: {bmr_w:.2f} calories/day")
    print(f"Chocolate bars needed for men: {bars_m}")
    print(f"Chocolate bars needed for women: {bars_w}")

    # Temperature Conversion
    print("\n--- Temperature Conversion ---")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")

    # Time Conversion
    print("\n--- Time Conversion ---")
    seconds = int(input("Enter number of seconds:"))
    h, m, s = seconds_to_hms(seconds)
    print(f"{seconds} seconds is equal to {h} hours, {m} minutes, and {s} seconds.")

if __name__ == "__main__":
    main()