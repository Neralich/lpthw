tabbed = "tabbed"
tabby_cat = "\tI'm %s in." % tabbed
line = "line"
persian_cat = "I'm split\non a %s." % line
I_am = "I'm"
a = "a"
animal = "cat"
backslash_cat = "%s \\ %s \\ %s." % (I_am, a, animal)

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
