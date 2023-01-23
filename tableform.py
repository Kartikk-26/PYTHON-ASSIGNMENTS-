# import module
from tabulate import tabulate

# assign data
mydata = [
	["KARTIK", "Delhi"],
	["HARSHAL", "Kanpur"],
	["MANAS", "Ahmedabad"],
	["KANIKA", "Bangalore"],
    ["MANASVI", "Chennai"],
]

# create header
head = ["Name", "City"]

# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))
