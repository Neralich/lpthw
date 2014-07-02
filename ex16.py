# this calls up a module aimed at holding information
from sys import argv
#these are the arguments to be held
script, filename = argv
# this just informs the user what is going to be done.
print "We're going to erase %r." % filename
# This gives user options - close program or run it.
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."
# this allows user to proceed or end (? is just the prompt)
raw_input("?")
# this just says what it is about to do
print "Opening the file..."
# this creates a variable and tells it to call the file (w says for it to be writable.)

target = open(filename, 'w')
# this just tells user the content is being deleted.
print "Truncating the file.  Goodbye!"
# this command removes content
target.truncate()
# this prompts user to enter strings
print "Now I'm going to ask you for three lines."
# three separate variables assigned to accept user input
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
# this informs user what is happening
print "I'm going to write these to the file."
# this writes the lines created above, "\n" starts each on a new line
target.write("%s\n%s\n%s" % (line1, line2, line3))
# this just explains the final action
print "And finally, we close it."
# this closes the program
target.close()