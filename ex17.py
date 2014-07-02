from sys import argv
from os.path import exists

script, original_file, new_file = argv

print "Copying from %s to %s" % (original_file, new_file)

# The following two lines could be combined
in_file = open(original_file).read()

print "The input file is %d bytes long." % len(in_file)

print "Does the output file exist? %r" % exists(new_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(new_file, 'w')
out_file.write(in_file)

print "Alright, all done."

out_file.close()
