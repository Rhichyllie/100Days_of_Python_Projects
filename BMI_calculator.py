height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    result = "Underweight"
elif BMI < 25:
    result = "Ideal Weight"
elif BMI < 30:
    result = "Overweight"
elif BMI < 35:
    result = "Obese"
else:
    result = "Clinically Obese"

print(f"Your BMI result is {BMI:.2f} and you are {result}")



