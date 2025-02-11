# Calculate BMR for men and women. Returns BMR values for both men and women.
def calculate_bmr(weight, height, age):
    bmr_men = (13.7516 * weight) + (5.0033 * height) - (6.755 * age) + 66.473
    bmr_women = (9.5634 * weight) + (1.8496 * height) - (4.6756 * age) + 655.0955
    return bmr_men, bmr_women 

# Calculate how many chocolate bars (214 calories each) are needed to maintain the BMR.
def chocolate_bars_needed(bmr): 
    return round(bmr / 214, 2)

if __name__ == "__main__":
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in cm: "))
    age = int(input("Enter age in years: "))

    bmr_m, bmr_w = calculate_bmr(weight, height, age)
    bars_m = chocolate_bars_needed(bmr_m)
    bars_w = chocolate_bars_needed(bmr_w)

    print(f"BMR fo men: {bmr_m:.2f} calories/day")
    print(f"BMR for women: {bmr_w:.2f} calories/day")
    print(f"Chocolate bars needed for men: {bars_m}")
    print(f"Chocolate bars needed for women: {bars_w}")