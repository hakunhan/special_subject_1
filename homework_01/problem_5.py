import utils.get_input

#getting the tract of land
total_square_feet = float(utils.get_input.number("Enter the total square feet of the tract of land: "))
#calculating acres
calculate_acres = f"{total_square_feet / 43500:.2f}"
print("The number of arches of that tract of land is: " + calculate_acres)