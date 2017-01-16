s = 'full'
tabby_cat = "\tI'm tabbed in %s." % s
persian_cat = "I'm split\non a line %r." % s
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''

I'll do a lsit:
\t* Cat food
\t* Fishes
\t* Catnip
\t* Grass

'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Rotating the slash

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
