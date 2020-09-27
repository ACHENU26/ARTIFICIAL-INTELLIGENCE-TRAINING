# -------------------------------------------------------------------------------
# FUNCTION
# -------------------------------------------------------------------------------
def calculateTheSurfaceToBeCleaned(zonesListe):
    surfaceToBeCleaned = 0
    for zone in zonesListe:
        lenght = zone.get("length") / 100
        width = zone.get("width") / 100
        calcul = lenght * width
        print(str(lenght) + "x" + str(width) + "=" + str(calcul))
        surfaceToBeCleaned = surfaceToBeCleaned + calcul
    return (surfaceToBeCleaned)


def timeToCleanInMinutes(surfaceToBeCleaned, timeForASquareMeter):
    return round(surfaceToBeCleaned * timeForASquareMeter)

# -------------------------------------------------------------------------------
# APPLICAITON
# -------------------------------------------------------------------------------

# Use of a tulp for the configuration of the application
# Robot name, time in minutes to clean a square meter
parameters = ("robot_hoover", 2)

# Depending on the type of room and furniture we have to cut the room by different zones.
# It becomes easy to calculate and calculate the total area to be cleaned by adding the areas of each zone.


# use of dictionaries for the creation of each zone
zone1 = {"length":500, "width":150}
zone2 = {"length":309, "width":480}
zone3 = {"length":101, "width":480}
zone4 = {"length":90, "width":220}

#Use of a list allowing you to store different zones within the same list
zones = []
zones.append(zone1)
zones.append(zone2)
zones.append(zone3)
zones.append(zone4)

# -------------------------------------------------------------------------------
# CALL THE FUNCTION
# -------------------------------------------------------------------------------

# Call of the function allowing to calculate the surface to be cleaned
surfaceToBeCleaned= calculateTheSurfaceToBeCleaned(zones)
print("The total surface to be cleaned is " + str(surfaceToBeCleaned) + "m2")

# Call of the function allowing to determine the cleaning time
estimatedTime =\
    timeToCleanInMinutes (surfaceToBeCleaned, parameters[1])
print("The estimated time is " + str(estimatedTime) + " minutes")

# Condition added that triggers according to the cleaning time
if estimatedTime > 55:
    print(parameters[0] + " I think it will take time !")
