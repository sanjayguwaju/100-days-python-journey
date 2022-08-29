#Don't change the code below
two_digit_number = input("Type a two digit number \n")
#############################################
#Write your code below this line
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

add_digits = int(first_digit) + int(second_digit)

convert_digit_type = str(add_digits)

print("Addition of 2 digits is :" + convert_digit_type)
