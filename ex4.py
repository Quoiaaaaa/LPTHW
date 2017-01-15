# add a value for cars
cars = 100
space_in_a_car = 4
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avargage_passangers_per_car = passangers / cars_driven

print "There are", cars, "cars avalable."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "emty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passangers, "to carpool today."
print "We need to put about", avargage_passangers_per_car, "in each car."
print "Hey %s there." % "you"
