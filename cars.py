# Create an empty set named showroom.

showroom = set()

# Add four of your favorite car model names to the set.

showroom = {"model s", "camaro", "DB11", "B7"}
print(showroom)

# Print the length of your set.
print("length of set",len(showroom))

# Pick one of the items in your show room and add it to the set again.

showroom.add("B7")

# Print your showroom. Notice how there's still only one instance of that model in there.

print(showroom)

# Using update(), add two more car models to your showroom with another set.

showroom_two = {"Q7", "QX70"}
showroom.update(showroom_two)
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.

showroom.discard("camaro")
print(showroom)


# Acquiring more cars

# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full
#  of old cars has approached you about buying the entire inventory. In the new set, add 
# some different cars, but also add a few that are the same as in the showroom set

junkyard = {"S550", "745Li", "LS460", "B7", "model s", "DB11"}
print("intersection", junkyard.intersection(showroom))

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.

print("union",showroom.union(junkyard))

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

showroom.discard("Q7")
print("discard", showroom)


