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
This module creates all the buttons for all perdiodic table elements.
Each button action shows a window with the element information.
All configuration is set by the class constructor and the window is managed by funcion "show".
The two functions remaining are used to configure the content and the place of the element button.
'''

# Project modules
from util.dimensions import x_positions, y_positions
from util.constants import C_0, C_1, EMPTY_STRING

# Python modules
from tkinter import Button, Toplevel, Label
from tkinter.font import Font

# Keywords
ATOMIC_NUMBER = "ATOMIC NUMBER"
COLOR = "CPK HEX COLOR"
SYMBOL = "SYMBOL"
ATOMIC_MASS = "ATOMIC MASS"
NAME = "NAME"
GROUP_BLOCK = "GROUP BLOCK"
GROUP = "GROUP"
PERIOD = "PERIOD"

# Button values.
BUTTON_FONT_FAMILY = "Arial Black"
BUTTON_FONT_SIZE = 15
BUTTON_WIDTH = 4
BUTTON_HEIGHT = 3

# Window data 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
WINDOW_LABEL_X_KEYS = 50
WINDOW_LABEL_X_VALUES = 400
WINDOW_LABEL_Y_BEGIN = 50
WINDOW_LABEL_Y_INCREASING = 25
WINDOW_FONT_FAMILY = "Courier New"
WINDOW_FONT_SIZE = 15

# Other constants
CHAR_LIMIT = 6
OPEN_PARENTHESIS = '('
LAWRENCIUM_ATOMIC_NUMBER = 103
LANTHANOID = "lanthanoid"
ACTINOID = "actinoid"

# Global
aux1, aux2 = C_0, C_0 # Used on 'get_button_place()'.

class Element:
    def __init__(self, button_window, element): # Class constructor.
        # Saving element dictionary.
        self.dictionary = element
        self.atomic_number = self.dictionary[ATOMIC_NUMBER] # it's used several times.
        self.color = self.dictionary[COLOR] # It's used several times.
        self.symbol = self.dictionary[SYMBOL] # Used in 'get_button_text()'.
        self.mass = self.dictionary[ATOMIC_MASS] # Used in 'get_button_text()'.
        self.name = self.dictionary[NAME].upper() # Used in 'show()'.
        self.group_block = self.dictionary[GROUP_BLOCK] # Used in 'get_button_place()'.
        self.x_index = self.dictionary[GROUP] # Used in 'get_button_place()'.
        self.y_index = self.dictionary[PERIOD] # Used in 'get_button_place()'.

        # Setting some button values.
        self.button_font = Font(family=BUTTON_FONT_FAMILY, size=BUTTON_FONT_SIZE)
        self.x, self.y = self.get_button_place() # Button X and Y positions.

        # Creating and setting element's button
        self.button = Button(button_window,
                            text=self.get_button_text(),
                            width=BUTTON_WIDTH,
                            height=BUTTON_HEIGHT,
                            font=self.button_font,
                            bg=self.color,
                            command=self.show).place(x=self.x, y=self.y)

        # Setting some window values
        self.window = None # Inital value
        self.window_font = Font(family=WINDOW_FONT_FAMILY, size=WINDOW_FONT_SIZE) # Element window labels font.

    def get_button_text(self): # Button's text getter.
        #String (Atomic Mass) fixing
        aux = str(self.mass)[:CHAR_LIMIT] # Characters limit shown in button. 
        mass = aux.replace(OPEN_PARENTHESIS, EMPTY_STRING) # Sometimes an open parenthesis is the last char shown in button so here we delete it.

        return f"{self.atomic_number}\n{self.symbol}\n{mass}" # Button's text

    def get_button_place(self):
        global aux1, aux2

        # Depending of group_block
        # There are 1 to 1 increments 'cause positions in collections begin in 0
        if self.group_block == LANTHANOID:
            self.y_index += C_1
            self.x_index += aux1 # This is for put Lanthanoids in their usual position
            aux1 += C_1
        elif self.group_block == ACTINOID:
            self.y_index += C_1
            self.x_index += aux2 # This is for put Actinoids in their usual position
            aux2 += C_1
        else:
            self.y_index -= C_1
            self.x_index -= C_1

        # Correcting stuff.
        if self.atomic_number == LAWRENCIUM_ATOMIC_NUMBER:
            # Last positions of each tuple will be the indexes
            self.y_index = y_positions.__len__() - C_1
            self.x_index = x_positions.__len__() - C_1

        # We got 'x' and 'y'!
        return x_positions[self.x_index], y_positions[self.y_index] # Button place

    def show(self): # Element button command runner.
        if self.window is None: # Element's window is not opened yet.
            self.window = Toplevel() # Element's window creation.
            self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}") # Element window size in pixels: "width x height".
            self.window.title(self.name) # Element window title.
            self.window.resizable(False, False) # Element window size change cancelation.

            Label(self.window, bg=self.color, width=WINDOW_WIDTH).place(x=C_0, y=C_0) # Decoration label.
            
            #Element window labels creation.
            y = WINDOW_LABEL_Y_BEGIN
            for key, value in self.dictionary.items():
                if key == COLOR: #Any key except "CPK HEX COLOR"
                    continue

                Label(self.window, text=key, font=self.window_font).place(x=WINDOW_LABEL_X_KEYS, y=y) # Key label.
                Label(self.window, text=f": {value}", font=self.window_font).place(x=WINDOW_LABEL_X_VALUES, y=y) # Value label.

                y += WINDOW_LABEL_Y_INCREASING
        else: # Element's window is already opened.
            self.window.destroy() # It closes element's window.
            self.window = None # Element's window is closed
            self.show() # Recursive function =)