# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = (round(weight / height ** 2)) 
bmi_2 = print(round(BMI,2))

if BMI  <= 100:
  if BMI < 18.5:
    print(f"Your BMI IS {BMI} you are Under weight")
  elif BMI < 25:
    print(f"Your BMI IS {BMI} you have Normal weight")
  elif BMI < 30:
    print(f"Your BMI IS {BMI} you are Slightly over weight")
  elif BMI >= 30:
    print(f"Your BMI IS {BMI} you are Obese")
else:
  print(f"Your BMI IS {BMI} you are Clinically obese")





