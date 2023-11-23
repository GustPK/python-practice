weight = float(input("Enter Your Weight : "))
height = float(input("Enter Your Height : "))

bmi = weight/((height/100)**2)
print("BMI is %.2f"%bmi)

if bmi >= 30 :
  print("Obesity")
elif bmi >= 25 :
  print("Overweight")
elif bmi >= 18.5 :
  print("Normal weight")
else :
  print("Underweight")