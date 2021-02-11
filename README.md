# Lindenmayer System
For my first steps into python I selected a Lindenmayer System (L-System). I had this as an assignment in university (in Java) and thought it was a great way to explore a new language.
L-Systems were introduced in 1968 by the biologist (and botanist) **Aristid Lindenmayer**. 

They describe the development and growth process of plants using a formal grammar with an initial axiom and a predefined set of rules to grow and construct multiple generations which can then be visualized. More information about L-Systems can be found in his book ["The algorithmic beauty of plants"](http://algorithmicbotany.org/papers/abop/abop.pdf)

### the second step <span style="font-size:0.5em">02/05/2021</span>
* *LSystemGenerator.py*
* *TurtleDrawer.py*
* *plant_structures.json*

In the next level I put all drawing functionality into a separate file, the *TrutleDrawer.py*. This file is then imported into the *LSystemGenerator.py* which handles all the main functionality. The rules are also in a separate json file to allow easy addition of more plants to choose from later on.

When starting the script, the user is asked to choose a plant from a list of all predefined plants which is extracted out of the json file. If something goes wrong in the selection process, a random plant is selected.
 
There are no real error handling or test features included. The functionality is realized using plain python, no extra packages except turtle.

### the first step <span style="font-size:0.5em">01/27/2021</span>
* *LSystem_plant.py*

My very first python program on GitHub. 
This first version has just one plant rule hard coded into the script. The visualization is conducted via turtle. You can play around with it by changing the number of generations and of course line_size and drawing_angle.
