group_height = input("Write the list of the group height: ").split()
for n in range(0, len(group_height)):
    group_height[n] = int(group_height[n])

total_height = 0
for height in group_height:
    total_height += height

total_people = 0
for group in group_height:
    total_people += 1

average_height = total_height / total_people
print(f"The average height is {average_height}")
