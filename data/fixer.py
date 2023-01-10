# Copyright 2023 Néstor Nahuatlato
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
This module uses data taken from -> https://documenter.getpostman.com/view/14793990/TzmCgD9k

The api before mentioned has an application error and it cannot be opened in web
so I brought the data to a JSON file ("raw_data.json") so that we can work with no problems.

We'll only modify the color values of all elements and change the keys to upper case.
After that, a new JSON file is created with the new information that we'll use for the rest of the project.
'''

from util.constants import C_1, EMPTY_STRING
from json import load, dumps

#Auxiliary dictionary for define button color.
#The element color is set by group block.
colors = {
    "alkaline earth metal" : "#AB5CF2",
    "alkali metal"         : "#EB0026",
    "transition metal"     : "#5CB8D1",
    "noble gas"            : "#F090A0",
    "nonmetal"             : "#FFFF30",
    "metalloid"            : "#9EAF51",
    "metal"                : "#3DFF00",
    "lanthanoid"           : "#94FFFF",
    "actinoid"             : "#1FFFC7",
    "halogen"              : "#DBDB56",
    "post-transition metal": "#60C73F"
}

#This function transforms the key text to upper case.
def key_fixing(key):
        #Auxiliary empty string.
        string = EMPTY_STRING

        #This 'for' puts a space before an upper letter.
        for char in key:
            if char.isupper():
                string += " "

            string += char

        #String in upper case.
        return string.upper()

#This function changes the color value in the element dictionary.
def color_fixing(group_block, atomic_number):
    color = "gray" #Default color.

    if atomic_number != C_1: #If actual element atomic number is not equal to hydrogen atomic number.
        for key, value in colors.items(): #Looking for a new color in the dictionary.
            if group_block == key: 
                color = value #Setting new color for the element.
                break

    return color

#Main function
if __name__ == "__main__":
    #Loading raw data from used api.
    with open("./raw.json", "r") as file:
        raw_data = load(file)
        file.close()

    my_elements = [] #List used to append new dictionaries.

    for element in raw_data: #Iterating in JSON.
        element = dict(element) #Every JSON element becomes a dictionary.
        element["cpkHexColor"] = color_fixing(element["groupBlock"], element["atomicNumber"]) #Modifying element color.

        my_element = {} #New dictionary used to save element information.
        for key, value in element.items(): #Iterating in element dictionary.
            my_element[key_fixing(key)] = value #Saving element information in dictionary.

        my_elements.append(my_element) #New dictionary appended.

    #Saving refreshed data to a new JSON file.
    with open("./fixed.json", "w") as new:
        new.write(dumps(my_elements, ensure_ascii=False, indent=4))
        new.close()