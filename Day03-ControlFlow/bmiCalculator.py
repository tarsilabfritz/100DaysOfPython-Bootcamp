height = 1.85
weight = 85

# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
elif 25 <= bmi < 30:
    print("overweight")
else:
    print("obese")
