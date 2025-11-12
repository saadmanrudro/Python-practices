# BMI Calculator by Saadman

print(" Welcome to the BMI Calculator ")

# Taking inputs from user
weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

# Formula
bmi = weight / (height ** 2)

# Show result
print(f"\nYour BMI is: {bmi:.2f}")

# BMI Categories
if bmi < 18.5:
    print(" You are underweight. Eat more protein & carbs!")
elif 18.5 <= bmi < 24.9:
    print(" You are healthy. Keep it up!")
elif 25 <= bmi < 29.9:
    print(" You are overweight. Need workouts!")
else:
    print(" You are obese. Please consult a doctor and start a fitness plan.")
