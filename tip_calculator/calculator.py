print("Welcome to the tip cakculator!\n")

total_bill = int(input("What was the price of the bill?\n"))

tip_number = int(
    input("How much in percent the tip will be?\nWrite a number like 12 or 5\n")
)

tip_percentage = tip_number / 100

number_of_people = int(input("How many people will split the bill?\n"))

final_number = total_bill * (tip_percentage + 1) / number_of_people

print(f"Each people should pay: {final_number}")
