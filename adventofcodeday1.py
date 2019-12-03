import math

def main():
	sum_fuel()

def sum_fuel():
	# Import file with mass list
	with open("adventofcodeday1") as file:
		total_fuel_needed = 0
		for line in file:
			total_fuel_needed = total_fuel_needed + calculate_fuel(int(line))
	print("Fuel Needed = {}".format(total_fuel_needed))


def calculate_fuel(mass):
	fuel = mass / 3
	fuel = math.floor(fuel)
	fuel = fuel - 2
	print("Fuel calculated from mass of '{}': {}".format(mass, fuel))
	return fuel

main()