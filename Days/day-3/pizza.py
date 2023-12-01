print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n") 
add_pepperoni = input("Do you want pepperoni? Y or N\n") 
extra_cheese = input("Do you want extra cheese? Y or N\n") 
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
total = 0

if size == "S":
    total +=15
elif size == "M":
    total +=20
else:
    total +=25

if add_pepperoni == "Y":
    if size == "S":
        total +=2
    else:
        total +=3

if extra_cheese == "Y":
    total +=1

print(f"That should be ${total}.")
