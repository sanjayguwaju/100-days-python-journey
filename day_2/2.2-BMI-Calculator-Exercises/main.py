#Don't change the code below👇
height = input("enter your height in m:")
weight = input("enter your weight in kg:")
#Don't change the code above👆

#Write your code below this line 👇
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
bmi_as_str = str(bmi_as_int)
print("Your BMI index is " + bmi_as_str)

