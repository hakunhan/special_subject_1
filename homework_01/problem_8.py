import utils.get_input

miles = float(utils.get_input.number("Enter the number of miles driven: "))
gallons_of_gas = float(input("Enter the number of gallons of gas used: "))

print(f"Car MPG is: {miles/gallons_of_gas:0.2f}")