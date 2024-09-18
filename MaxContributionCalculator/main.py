print("Hi, My name is Michael Marsillo and this is my first solo python project.")
print()
print("Essentially I decided to create a max contribution room calculator to help people that want to know how much money")
print("they can/still contribute to their TSFA savings account or mutual fund etc.")
print()
print("Hope you find my project helpful.")


# Input
year_of_start = int(input(f"In what year did you turn 18 years old?: "))
amount_deposited = int(input(f"How much have you contributed to your TFSA in total so far?: "))
amount_withdrawn = int(input(f"How much have you withdrawn from your TFSA in total so far?: "))

# Initialize contribution room
contribution_room = 0

# Loop through each year from the start year to 2024 and add the corresponding contribution limit
for year in range(year_of_start, 2025):
    if 2009 <= year <= 2012:
        contribution_room += 5000
    elif 2013 <= year <= 2014:
        contribution_room += 5500
    elif year == 2015:
        contribution_room += 10000
    elif 2016 <= year <= 2018:
        contribution_room += 5500
    elif 2019 <= year <= 2022:
        contribution_room += 6000
    elif year == 2023:
        contribution_room += 6500
    elif year == 2024:
        contribution_room += 7000

# Adjust for deposits and withdrawals
contribution_room = contribution_room - amount_deposited + amount_withdrawn

# Output
print(f"Your current contribution room is {contribution_room}$ ")
