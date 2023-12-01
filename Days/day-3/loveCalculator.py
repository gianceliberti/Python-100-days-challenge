print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
nombre_compuesto = name1 + name2
lower_nombre_compuesto = nombre_compuesto.lower()
t = lower_nombre_compuesto.count("t")
r = lower_nombre_compuesto.count("r")
u = lower_nombre_compuesto.count("u")
e = lower_nombre_compuesto.count("e")

first_digit = t + r + u + e

l = lower_nombre_compuesto.count("l")
o = lower_nombre_compuesto.count("o")
v = lower_nombre_compuesto.count("v")
e = lower_nombre_compuesto.count("e")

second_digit = l+ o + v + e

score = int(str(first_digit) + str(second_digit))

if score > 90 or score < 10:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")