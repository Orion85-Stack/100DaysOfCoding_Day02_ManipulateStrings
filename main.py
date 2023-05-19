print("Data Types")

#Count from 0 in Python to find the index position
print("Hello"[0])

#first convert the numeric to str then can use the
#len function
print(len(str(12345869)))

num_char = len(input("What is your name? "))
print(type(num_char)) # Cannot use int in concat
print(num_char)

num_char_2 = len((input("What is your name? \n")))
str_num = str(num_char_2)
print(type(str_num))
print("Your name is " + str_num + " characters long")

#Challenge
main_number = str(input("Pick any double digit number: "))
sub_number_1 = str(main_number[0])
sub_number_2 = str(main_number[1])

print(f"{sub_number_1} + {sub_number_2}")
print(int(sub_number_1) + int(sub_number_2))
# print(sub_number_1)
# print(sub_number_2)

print("-" * 90)

print("Challenge : BMI Calculator")

weight = int(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meter: "))

bmi = weight / height**2

print("Your BMI index is : ")
print(int(bmi))

print("-" * 90)
print("Life in Weeks")

age = int(input("What is your age? "))

age_days = age * 365
age_months = age_days / 30
age_weeks = age_days / 52

age_90_days = 90 * 365
age_90_months = age_90_days / 30
age_90_weeks = age_90_days / 52

# print(age_days)
# print(round(age_weeks))
# print(round(age_months))

days_left = round(age_90_days - age_days)
weeks_left = round(age_90_weeks - age_weeks)
months_left = round(age_90_months - age_months)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left to live to 90.")
