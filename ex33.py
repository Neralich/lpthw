# This is the initial script

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for i in numbers:
	print i

# 1. This is the first study drill - convert while-loop to function
print "\nConverting while-loop to function, drill_1"
def drill_1(n):
	i = 0
	numbers1 = []
	while i < n:
		print "Item: %d" % i
		numbers1.append(i)
		i = i + 1
	print numbers1

# 2. This is the second study drill - try function with two values
print "\nUsing drill_1 with n = 4"
drill_1(4)

print "\nUsing drill_1 with n = 3"
drill_1(3)

#3. This is the third study drill - adding extra variable to function

def drill_3(n, s):
	i = 0
	numbers3 = []
	while i < n:
		print "Item: %d" % i
		numbers3.append(i)
		i = i + s
	print numbers3

print "\nUsing drill_3 with n = 3 and s = 2"
drill_3(3, 2)

# 4. This is the fourth study drill - changing to for-loops/range

print "\nUsing drill_4 w/ a for-loop and range instead."
def drill_3 (n, s):
	numbers_4 = range(0, n, s)
	for i in numbers:
		print "Item: %d" % i
	print numbers_4

drill_3(14, 4)