students = ["Samarth", "Max", "Tianji"]
students.sort()
first_name = students[0]
first_name = first_name[:-1]
print(first_name)


size = 0
new_name = ""

for x in students:
	if len(x) > size:
		new_name = x
		size = len(x)

print(new_name)