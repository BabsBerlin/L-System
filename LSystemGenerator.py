from TurtleDrawer import *
import os
import json
import random

# define the plant parameter
# the plants work best with an angle of 22.5, the snowflake needs 60
generations = 4
line_size = 5
drawing_angle = 22.5 

# import the plant parameters from the external json file
filename = "plant_structures.json"
with open(os.path.dirname(os.path.realpath(__file__))+"\\"+filename) as json_file:
    data = json.load(json_file)
json_file.close()

# extract all plant names out of the plant parameters
names = []
for p in data["plants"]:
    names.append(p["name"])
plant_choices = ', '.join(names)

# ask the user to choose one of the provided plants
plant_type = input("*** INPUT REQUIRED *** Which plant should be generated, please choose from the following options: "+plant_choices+" : ")

# if the user input was incorrect, choose a random plants 
if str(plant_type) not in names:
    print("not in list")
    plant_type = random.choice(names)
    print(plant_type)

# extract all parameters for the choosen plant
for p in data["plants"]:
    if str(p["name"]) == plant_type:
        plant_name = p["name"]
        plant_axiom = p["axiom"]
        plant_rules = p["rules"]
# prepare the ruleset for generating the plant
plant_rules = plant_rules.replace("{","")
plant_rules = plant_rules.replace("}","")
ruleset = plant_rules.split(",")

# the L-System generator
def generate_lsystem(generationX, generation_count):
    generation_count += 1
    newGen = ""
    if generation_count > generations:
        return generationX
    else:
        for letter in generationX:
            flag = False
            for rule in ruleset:
                rule = rule.split(":")
                if letter == rule[0] and flag == False:
                    newGen = newGen.__add__(str(rule[1]))
                    flag = True
            if flag == False:
                newGen = newGen.__add__(str(letter))
        print("Generation "+str(generation_count)+" : "+newGen)
        return generate_lsystem(newGen, generation_count)


# apply the generator to create the plant
final_system = generate_lsystem(plant_axiom, 0)

# draw the plant
myTurtle = initializeTurtleDrawer()
draw(myTurtle, final_system, line_size, drawing_angle)