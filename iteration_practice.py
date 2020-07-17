"""
#Iterate through user input of names.

names = input("Enter five names separated by a space here: ")
namesList = names.split()
for name in namesList:
    print(name, " is awesome!")
    
###############################
"""
#Iterate through list of planets but exclude pluto.
planets = ["earth","jupiter","neptune",
           "mars","pluto","saturn",
           "venus","mercury","uranus"]

for planet in planets:
    if (planet == "pluto"):
        continue
    print(planet)



