#convert date format mm/dd/yyyy to Month Day, Year
#i.e: 03/21/2000 to March 21, 2000

#dictionary of month
MONTH_DICT = {	'01':'Janauary',
		'02':'February',
		'03':'March',
		'04':'April',
		'05':'May',
		'06':'June',
		'07':'July',
		'08':'August',
		'09':'September',
		'10':'October',
		'11':'November',
		'12':'December'		}

#print converted (assume user input correct format)
def print_date(date):
    date_list = list(date.split("/"))

    month = MONTH_DICT[date_list[0]]
    print(f"{month} {date_list[1]}, {date_list[2]}")

def main():
    date = input("Enter the date in format mm/dd/yyyy: ")
    print_date(date)

main()