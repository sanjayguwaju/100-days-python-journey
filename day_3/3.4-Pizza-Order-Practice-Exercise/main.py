#Don't change the code below
print("Welcome to the Python Pizzas Deliveries!")
size = input("What size do you want? S,M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
#Don't change the code above

#Write code below this line
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill amount is ${bill}")
