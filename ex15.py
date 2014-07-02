# this line is a module that instructs python to "hold" information
from sys import argv

# this is to input the arguments
script, filename = argv

# this is creating the variable "txt" and telling it to fetch the file.
txt = open(filename)

# this is just a line to explain what is happening.
print "Here's your file %r." % filename
# this is issuing a command to the file - here it prints it
print txt.read()
txt.close()

# this is asking for user input.
print "Type the filename again."
# this creates a new variable and sets it equal to the filename typed by the user (same name as above)
file_again = raw_input("> ")

# this creates a new variable and tells it to fetch the file entered by the user
txt_again = open(file_again)
# this prints what is in the file fetched by the user
print txt_again.read()
txt_again.close()
