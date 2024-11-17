blue = [(100,200), (105,205),(99,100)]
red = [(500,0),(450,10),(470,20)]


test = (int(input("Input the first value\t")),int(input("Input the second value\t")))

min_blue = 10000000000000
min_red = 10000000000000
for _ in blue:
	if((_[0] - test[0])**2 +(_[1] - test[1])**2) < min_blue:
		min_blue = (_[0] - test[0])**2 +(_[1] - test[1])**2

for _ in red:
	if((_[0] - test[0])**2 +(_[1] - test[1])**2) < min_red:
		min_red = (_[0] - test[0])**2 +(_[1] - test[1])**2

print(f"Blue is {min_blue} far from test")
print(f"Red is {min_red} far from test")

if(min_blue < min_red):
	print("We guess it is blue")
else:
	print("We guess it is red")
