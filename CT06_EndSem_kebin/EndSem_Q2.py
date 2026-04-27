#list:
planets = ["mercury","venus", "earth", "mars", "jupiter", "saturn", "uranus"]
print(planets[2])
#list(add neptune,change mars to muskworld and remove uranus):
planets.append("neptune")
planets[3] = "muskworld"
planets.remove("uranus")
for planet in planets:
    print(planet)