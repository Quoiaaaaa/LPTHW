x = "There are %d types of people." % 10 #create new value "x". Insert into double-quotes a format characters that put into text the value of 10
binary = "binary" #create value with string data binary
do_not = "don't" #create value with string daya don't
y = "Those who know %s and those who %s." % (binary,do_not) #formated charaters will be print on the display one. First binary in the plase %s and do_not insted second %s

print x #print string from varible x with text instead formated characters
print y #print string from varible y with text instead formated charaters

print "I said: %r." % x #instead %r will be print string from value x
print "I also said: '%s'." % y #instead %s will be print string from value y

hilarios = True # binary parameter
joke_evaluation = "Isn't that joke so funny ?! %r"

print joke_evaluation % hilarios # print joke_evaluation with bolean parameter instead % r

w = "This is the left side of..."
e = "a string with a right side."

print w + e # concatenatio of two string w and e
