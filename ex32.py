# IMPORTANT: At first, try to always use "i" as the variable.  
# Think of it as the word "items"
# Ex. for i(tems) in the_count: ...

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for i in the_count:
	print "This is count %d" % i

for i in fruits:
	print "A fruit of type: %s" % i

for i in change:
	print "I got %r" % i

elements = []

# With ranges, it includes the first number, but NOT the second
# So, in the following range, it will include 0 - 5
for i in range(0, 6):
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i

# An easier way to do the above example is:

# elements = range(6)
# for i in elements:
#	print "Element was: %d" % i
