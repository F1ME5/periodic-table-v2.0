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
This module contains two funcionts that set values used as dimensions.
'''

from util.constants import C_0, C_1

'''
This funtion is used to generate a tuple that contains all integer values
for place buttons horizontally and vertically in the window.

All 'x' and 'y' buttons positions were set by constants increasings
and other values that are defined in "element.py".

Those parameters are set in 'dimensions.py'.
'''

Y_CORRECTION = 30

def get_positions(increasing, begin, max, flag):
    positions = []

    x = begin #First 'x'
    positions.append(x) #First 'x' appended
    for i in range(max): #It'll repeat 'max' times
        x += increasing #Next 'x' is equal to previous 'x' plus increasing
        positions.append(x) #Next 'x' appended

    if flag:#We're working with 'y_positions' (used in element.py)
        #Y_CORRECTION is used to separate for some height pixels elements 57-71 and 89-103
        positions[max - C_1] += Y_CORRECTION #Lanthanoids
        positions[max] += Y_CORRECTION #Actinoids

    return tuple(positions) #Returning the list as a tuple

'''
This function is used to get the periods and groups labels positions.
The two collections received as parameters were created in 'dimensions.py' using 'get_positions()'.
'''
def get_labels_positions(x_positions, y_positions):
    groups_positions = {}

    i = C_0
    for x in x_positions:
        if i == C_0 or i == (len(x_positions) - C_1): # Group label for groups 1 and 18
            y = y_positions[C_0]
        elif i == C_1 or (11 < i < 17): # Group label for groups 2 and from 13 to 17.
            y = y_positions[C_1] 
        else: # Group label for groups from 3 to 12.
            y = y_positions[3]

        groups_positions[x] = y
        i += C_1

    # Returning the dictionary.
    # 'y_positions' is cut 'cause there are 7 periods on periodic table.
    return groups_positions, y_positions[:7]