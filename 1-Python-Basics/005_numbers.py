# Working with numbers

# int type
lives = 3
print(type(lives))
age = 12

# float type
budget = 100.0
print(type(budget))

lives = 2
print(f"lives: {lives}")
lives = 1
print(f"lives: {lives}")

lives = 12 + 15
print(f"lives: {lives}")

lives = lives - 1
print(f"lives: {lives}")
# This does the same:
lives -= 1
print(f"lives: {lives}")

lives += 2
print(f"lives: {lives}")

# Cientific notation: (when a number is big enough, python translates it to cientific notation
number = 4500000000000000000000000.1
print(number)

number2 = 0.000000000000005
print(number2)
numer3 = 4.56
print(round(numer3))


### Chalenge | average:

#jan_budget = 10000
#feb_budget = 20000
#march_budget = 15000

#avg_budget = (jan_budget + feb_budget + march_budget) / 3
#print(f"The average budget for jan, feb and march was: {avg_budget}")

print("")
print("----Starts program execution----")

jan_budget = input("Please enter january's budget: ")
feb_budget = input("Please enter january's budget: ")
march_budget = input("Please enter january's budget: ")

avg_budget = (int(jan_budget) + int(feb_budget) + int(march_budget)) / 3
print(f"The average budget for jan, feb and march was: {avg_budget}")