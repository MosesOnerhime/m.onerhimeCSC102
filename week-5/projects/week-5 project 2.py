# Get the inputs
experience = int(input("How many years of experience do you have? : "))
age = int(input("What is your current age? : "))

# Make the conditions for the ATR
if (experience > 25) and (age >= 55):
    atr = "N5,600,000.00"

elif (experience > 20) and (age >= 45):
    atr = "N4,480,000.00"

elif (experience > 10) and (age >= 35):
    atr = "N1,500,000.00"

elif (experience <= 10) and (age < 35):
    atr = "N550,000.00"

print(f"Your annual tax revenue(ATR) is {atr}.")

