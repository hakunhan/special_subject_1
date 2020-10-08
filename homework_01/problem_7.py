import utils.get_input

amount_purchase = float(utils.get_input.number("Enter the amount of a purchase: "))
state_tax = amount_purchase * .05
county_tax = amount_purchase * 0.025
total_sale_tax = state_tax + county_tax
total_sale = amount_purchase + total_sale_tax

print(f"The amount of purchase: {amount_purchase}, state sales tax: {state_tax},\n"
      f"country sales tax: {county_tax}, total sales tax: {total_sale_tax},\n"
      f"and the total of the sale: {total_sale}")