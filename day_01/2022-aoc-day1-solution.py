
"""
Thought process...
what is the total cal of largest elf
How many total Calories is that Elf carrying?
loop on each item 
break on newline
if > elf-cal-total neow that elf is the max
elftotal 
read in from input.txt
"""


input_file_name = "input.txt"
sum_calories = 0
max_calories = 0
elves = []
with open(input_file_name, "r") as fp:
    lines = fp.readlines()
for line in lines:
    #print(line)
    if line == "\n":
        #print(f"appending {sum_calories} to elves")
        elves.append(sum_calories)
        sum_calories = 0
    else:
        calories = int(line)
        #print(f"adding {calories} to sum")
        sum_calories += calories
        #print(sum_calories)
if sum_calories != 0:
    elves.append(sum_calories)
print(f"The Elvish Totals: {elves}")
elves.sort(reverse=True)
print(f"The Top Three Elves: {elves[0:3]}")
print(f"The Sum of of the Top Three Elves: {sum(elves[0:3])}")