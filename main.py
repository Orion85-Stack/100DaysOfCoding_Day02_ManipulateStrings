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